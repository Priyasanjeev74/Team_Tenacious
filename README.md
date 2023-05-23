# Team_Tenacious
Detecting angle between two flat objects
This project is done in Hackathon under 24hrs in RGMCET

In this repository, we are gonna calculate angle between two flat objects The main objective of the code is to detect objects in a live video stream and calculate the angle of the detected object.

The necessary libraries, cv2 (OpenCV) and numpy, are imported.

The edge_detection function takes an image as input and performs edge detection using the Canny edge detection algorithm. It converts the image to grayscale, applies Gaussian blur, and then detects edges using Canny edge detection. The resulting edge image is returned.

The draw_lines function is responsible for drawing lines on the image. It takes the image, a set of lines, color, and thickness as inputs. It iterates through the lines and draws each line on the image using the cv2.line function. Additionally, it handles cases where the line is vertical, drawing a vertical line from top to bottom of the image.

The get_angle function calculates the angle of the detected object in the image. It converts the image to grayscale, applies Canny edge detection, and uses the Hough transform to detect lines in the edge image. The detected lines are then iterated, and for each line, the function calculates the angle using trigonometry. The angle is returned.

The code initializes the video capture using cv2.VideoCapture(0), which captures video from the default camera.

A while loop is used to continuously read frames from the video capture. Inside the loop, the frame is displayed using cv2.imshow. The loop breaks if the user presses the 'q' key.

Another while loop is used to detect an object and calculate its angle. This loop continues until an object is detected or the user presses the 'q' key. Inside the loop, a frame is read from the video capture, and the get_angle function is called to calculate the angle. If an angle is obtained, it is printed, and the loop is terminated. The frame is displayed, and the loop breaks if the user presses the 'q' key or 's' key to save the frame as an image.

After the loops end, the video capture is released, and all windows are closed using cap.release() and cv2.destroyAllWindows().

**INSTALLED MODULES :**

NumPy

OpenCV

Time

Matplot

**APPLICATIONS :**


Real-time Object Detection

Flexibility

Real-time Visualization

Image Saving

Platform Independence

Gaming

VR

Construction


**TEAM MEMBERS:**


Lokesh J(Lead)

Nanda Kishore R

Tejaswini M

Hussain S

Subhash

Priyanka R

Muni Kishore P


**CONCLUSION:**


The goal of Angle Detection task is to detect an angle between 2 flat objects in a single image or video sequence. The accuracy of the algorithm depends upon different factors like the camera used, the size of objects, clarity of the image and accurate position. Angle detection is often combined with other factors like define an object,determining a reference point, measure the reference lines and apply trignometry to develop more robust applications that better solve real-life scenarios.

**ACKNOWLEDGEMENT:**

We would like to acknowledge and thank RGMCET and BYTS INDIA for their efforts in organizing the 24-hour hackathon, which brought us together for an exciting event. We are immensely grateful for their commitment to fostering learning, collaboration, and growth. At last this event gave us an unique and enriching experience.


**CONTACT:**

 
For any queries and feedback contact
priyankaraminepalli@gmail.com
