# Human Detection and SMS Alert System Using OpenCV and Twilio

## Introduction
This Python script uses OpenCV and cvzone's PoseModule to detect the presence of a human in a video feed. If a human is detected continuously for a certain number of frames, the script triggers an SMS alert using the Twilio API.

## Requirements
Before running the script, ensure you have the following dependencies installed:

### Python Libraries:
- OpenCV (`cv2`): `pip install opencv-python` 
- cvzone (`PoseModule`): `pip install cvzone`
- Twilio (`twilio.rest`): `pip install twilio`

### Hardware Requirements:
- A working webcam or an external camera.

## Code Explanation

### Importing Required Libraries
```python
import cv2
from cvzone.PoseModule import PoseDetector
import send
```
- `cv2` is used for handling the video stream.
- `PoseDetector` from `cvzone.PoseModule` is used for detecting human poses.
- `send` is a custom module that contains the `sendSms()` function.

### Initializing Camera and Pose Detector
```python
detector = PoseDetector()
cap  = cv2.VideoCapture(0)
cap.set(3,640)  # Set width
cap.set(4,480)  # Set height
```
- Initializes the `PoseDetector()`.
- Captures video from the default camera (`0`).
- Sets the video frame width and height.

### Processing Video Stream
```python
l=[]  # List to store detection count
flag=True  # Flag to prevent multiple SMS triggers

while True:
    success,img = cap.read()
    img = detector.findPose(img)  # Detect pose
    imlist, bbox = detector.findPosition(img)  # Get detected position
    
    if len(imlist) > 0:
        print("Human detected")
        l.append(1)
    
    if len(l) > 50 and flag:
        flag = False  # Prevents multiple alerts
        send.sendSms()

    cv2.imshow("Output" , img)
    q = cv2.waitKey(1)
    if q == ord('q'):
        break
```
- Reads frames from the camera.
- Detects human presence.
- If a human is detected, it logs the event.
- If a human is detected for more than 50 frames, an SMS is triggered.
- The loop runs until the user presses 'q'.

### Sending SMS Using Twilio
```python
from twilio.rest import Client

def sendSms():
    account_sid = ''
    auth_token = '[AuthToken]'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='[]',
        body='Enter your message' ,
        to='[]'
    )
    print(message.sid)
```
- Uses Twilio's API to send an SMS alert.
- Requires valid Twilio credentials (`account_sid`, `auth_token`).
- Sends an SMS when triggered.

## Improvements & Considerations
1. **Security:** Avoid hardcoding Twilio credentials. Use environment variables or a configuration file.
2. **Threshold Optimization:** The detection threshold (50 frames) can be adjusted based on application needs.
3. **Efficiency:** Instead of appending to a list, use a counter to track continuous detections.
4. **Error Handling:** Implement exception handling for Twilio API failures and camera errors.

## Conclusion
This script effectively detects a human using OpenCV and triggers an SMS alert when a person is continuously detected for a certain period. It can be improved by optimizing detection logic, enhancing security, and adding additional features like email alerts or database logging.

