import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
from skimage.transform import hough_line, hough_line_peaks


def edge_detection(img, blur_ksize=3, threshold1=50, threshold2=50):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gaussian = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)
    img_canny = cv2.Canny(img_gaussian, threshold1, threshold2)

    return img_canny
def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                if x2 - x1 == 0:
                    cv2.line(img, (x1, 0), (x1, img.shape[0]), color, thickness)
                else:
                    # calculate slope and y-intercept
                    m = (y2 - y1) / (x2 - x1)
                    b = y1 - m * x1

                    # calculate endpoints of line at top and bottom of image
                    y_top = 0
                    x_top = (y_top - b) / m
                    y_bottom = img.shape[0]
                    x_bottom = (y_bottom - b) / m

                    # draw line
                    cv2.line(img, (int(x_top), y_top), (int(x_bottom), y_bottom), color, thickness)
def get_angle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    # extract the angle
    angle = 0
    if lines is not None:
        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                angle = np.arctan2(y2 - y1, x2 - x1)
                angle = angle * 180 / np.pi
                angle = abs(angle)
                if angle > 180:
                    angle = 360 - angle
        if angle != 0:
            return angle
    return None


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    angle = get_angle(frame)
    if angle is not None:
        print("Angle: {:.2f}".format(angle))
        break # stop capturing frames after the object is detected

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# capture an image from the default camera
cap = cv2.VideoCapture(0)

# check if the camera is opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# capture a frame from the camera
ret, frame = cap.read()

# check if the frame is captured successfully
if not ret:
    print("Cannot capture frame")
    exit()

# crop the captured image to a fixed rectangle around the center of the frame
height, width = frame.shape[:2]
crop_size = 200
x1 = int((width - crop_size) / 2)
y1 = int((height - crop_size) / 2)
x2 = x1 + crop_size
y2 = y1 + crop_size
frame = frame[y1:y2, x1:x2]

# get the angle between the detected lines in the captured image
angle = get_angle(frame)

# release the camera
cap.release()

# plot the image with detected lines (for visualization only)
image = edge_detection(frame)
h, theta, d = hough_line(image)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax = axes.ravel()

ax[0].imshow(frame)
ax[0].set_title('Input image')
ax[0].set_axis_off()

ax[1].imshow(image, cmap=plt.cm.gray)
for _, a, d in zip(*hough_line_peaks(h, theta, d)):
    y0 = (d - 0 * np.cos(a)) / np.sin(a)
    y1 = (d - image.shape[1] * np.cos(a)) / np.sin(a)
    ax[1].plot((0, image.shape[1]), (y0, y1), '-r')

plt.tight_layout()
plt.show()