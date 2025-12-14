# 💻 Face Recognition System with OpenCV, MediaPipe, and `face_recognition`

This project implements a **real-time face recognition system** capable of identifying known individuals from a database and registering new, unknown faces on the fly. It is built using popular Python libraries for computer vision and machine learning.

## 🌟 Table of Contents
1. [Features](#features)
2. [Demo](#demo)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [How to Use](#how-to-use)

## ✨ Features

* **Real-Time Detection and Recognition:** Utilizes the device camera to detect faces in real-time.
* **Database Integration:** Compares detected faces against a stored database of known face encodings and names.
* **Dynamic Registration:** Allows users to **register new faces** that are identified as "Unknown," storing their face encoding and name for future recognition.
* **Visual Feedback:** Draws a bounding box around the detected face and displays the **recognized name** (or "Unknown") above the box.
* **Efficient Encoding:** Leverages the power of the `face_recognition` library (built on dlib) for highly accurate face encoding and comparison.

## 🎬 Demo

> The application starts the camera feed. When an unknown face is detected, you can press 'o' on keyboard then a prompt appears to enter the person's name. Once entered, the system saves the face data. The next time the face is seen, the recognized name is displayed in the bounding box.

## 🛠️ Technologies Used

| Category | Library | Purpose |
| :--- | :--- | :--- |
| **Main CV Framework** | **OpenCV (`cv2`)** | Handles video stream capture, image manipulation, and displaying the output. |
| **Face Detection** | **MediaPipe** | Used for robust and fast initial face detection. |
| **Face Recognition** | **`face_recognition`** | Generates 128-dimensional face encodings and performs the comparison. |
| **Data Handling** | **pickle** | Used for persistent storage of face encodings and names. |
| **Language** | **Python 3.11** | The core language used for the entire application. |

## 🚀 Setup and Installation

### Prerequisites

* Python 3.10+
* `pip` package manager
* **System Dependencies for `dlib`:** On some systems, you may need to install development libraries, CMake, and a C++ compiler.

### Clone the Repository

```bash
git clone [https://github.com/YourUsername/YuTVO.git](https://github.com/YourUsername/YuTVO.git)
cd YuTVO
```

## How to use

* Change you camera ID in program code
* Run program
* To make program recognize faces press 'o' button on keyboard
* Enter names according to label
* Click 'Ok' button
