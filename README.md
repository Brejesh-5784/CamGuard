
# **Human Detection and SMS Alert System**

### *Using OpenCV, cvzone, and Twilio*

---

## **📌 Overview**

This project is a **real-time human detection and alert system** that uses **OpenCV** and **cvzone's PoseModule** to detect the presence of humans in a live video stream.
When a person is detected **continuously for a specified number of frames**, an **SMS alert** is triggered using the **Twilio API**.

This solution can be applied in various domains, such as:

* Railway trespassing detection
* Restricted area monitoring
* Home or office surveillance
* Public safety and security

---

## **⚙️ Key Features**

* 🎥 **Real-time video processing** using OpenCV
* 🧍 **Human detection** using pose estimation
* 📩 **Automated SMS alerts** via Twilio
* 🎚️ Adjustable detection threshold based on frame count
* 🛡️ Secure Twilio credentials using environment variables
* 🚨 Prevents **multiple alerts** during a single detection event
* 🛠️ Modular project structure for better maintainability

---

## **🛠️ Requirements**

### **1. Software & Libraries**

* **Python** (3.8 or above)
* **OpenCV** → for real-time video capture and processing
* **cvzone** → for pose detection
* **Twilio API** → for sending SMS alerts
* **dotenv** → for securing credentials

### **2. Hardware**

* A working **webcam** or **external camera**.

### **3. Twilio Setup**

* Create a **Twilio account**.
* Get your **Account SID**, **Auth Token**, and **Twilio phone number**.
* Save these credentials securely using a `.env` file.

---

## **📂 Project Structure**

```
human-detection-alert/
│── main.py             # Handles camera feed, human detection, and SMS triggering
│── send.py             # Contains Twilio integration for sending alerts
│── .env                # Stores Twilio credentials securely
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
```

---

## **🔄 How It Works**

1. **Video Capture** → The system continuously captures video frames using OpenCV.
2. **Pose Detection** → `cvzone.PoseModule` analyzes each frame to detect humans.
3. **Frame Counting** → If a human is detected, a **counter** tracks consecutive frames.
4. **Threshold Check** → Once the detection threshold is crossed, an **alert is triggered**.
5. **SMS Notification** → Twilio sends an SMS to the configured recipient.
6. **Single Alert Control** → The system avoids sending duplicate messages for the same detection.

---

## **🔐 Security Measures**

* **No hardcoded credentials** → Uses a `.env` file.
* **API key protection** → Environment variables are kept out of source control.
* **Error handling** → Ensures camera and Twilio API failures are managed gracefully.

---

## **📌 Improvements Over Previous Version**

| **Aspect**          | **Old Version**         | **Updated Version**          |
| ------------------- | ----------------------- | ---------------------------- |
| Credential Handling | Hardcoded in code ❌     | Uses `.env` ✅                |
| Detection Method    | List-based counting ❌   | Optimized frame counter ✅    |
| Alert Control       | Multiple SMS possible ❌ | Single alert per detection ✅ |
| Code Structure      | Single-file script ❌    | Modular, cleaner code ✅      |
| Logging & Status    | Minimal ❌               | Detailed logs ✅              |
| Scalability         | Limited ❌               | Easily extendable ✅          |

---

## **🚀 Usage Workflow**

1. **Install dependencies** using `pip install -r requirements.txt`.
2. **Set Twilio credentials** in the `.env` file.
3. **Run the system** to start real-time monitoring.
4. **Monitor detection** via live video feed.
5. **Receive SMS alerts** when continuous detection occurs.

---

## **💡 Possible Future Enhancements**

* **WhatsApp integration** for free alerts via Twilio
* **Email notifications** for multi-channel alerts
* **Database logging** to track detection history
* **Cloud deployment** for remote monitoring
* **IoT integration** with alarm systems
* **Multi-camera support** for wider surveillance

---

## **🎯 Conclusion**

This project provides an efficient, **real-time human detection and alert system** using OpenCV and Twilio.
With its **secure design**, **optimized detection logic**, and **scalable architecture**, it is suitable for multiple real-world applications, including **railway trespassing detection**, **security monitoring**, and **automated surveillance**.


