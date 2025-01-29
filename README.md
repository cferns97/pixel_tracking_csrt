# CSRT Object Tracker with OpenCV and Webcam

A real-time object tracker using OpenCV's **CSRT Tracker**.  
The tracker allows you to start and stop tracking an object using **left-click**.

## Features
✅ Uses **OpenCV's CSRT Tracker** for accurate object tracking.  
✅ **Left-click to start and stop tracking**.  
✅ Displays real-time video feed from the webcam.  
✅ Simple and modular **Python codebase** for easy modifications.  

## Installation

Ensure you have Python 3 installed and the libraries in `requirements.txt`:

```sh
pip3 install -r requirements.txt
```

## Usage

Run the script with:

```sh
python3 main.py
```

### **Controls**
- **Left-click** anywhere on the screen to **start tracking** (100x100 box centered at click).
- **Left-click again** to **stop tracking**.
- **Press 'q'** to **exit** the application.