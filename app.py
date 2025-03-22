import cv2
from cvzone.PoseModule import PoseDetector  # Importing PoseDetector for human detection
import send  # Importing custom module to send SMS alerts

# Initialize pose detector
detector = PoseDetector()

# Initialize webcam capture
cap = cv2.VideoCapture(0)  # 0 for default camera
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

l = []  # List to store frame-based human detection count
flag = True  # Flag to prevent multiple SMS alerts

while True:
    success, img = cap.read()  # Read a frame from the camera
    img = detector.findPose(img)  # Detect pose in the frame
    imlist, bbox = detector.findPosition(img)  # Get detected keypoints and bounding box
    
    if len(imlist) > 0:  # Check if any human is detected
        print("Human detected")
        l.append(1)  # Log detection occurrence
    
    # Check if human detected for more than 50 frames and flag is still True
    if len(l) > 50 and flag:
        flag = False  # Prevent multiple alerts
        send.sendSms()  # Send SMS alert
    
    cv2.imshow("Output", img)  # Display the processed frame

    # Break loop when 'q' key is pressed
    q = cv2.waitKey(1)
    if q == ord('q'):
        break
