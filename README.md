---
# Detect, Track, and Count Cars and Motorcycles Using Background Subtraction
## Project Overview

This project implements a system for detecting, tracking, and counting cars and motorcycles in a video feed using OpenCV. The system utilizes background subtraction to detect moving objects and Euclidean distance tracking to keep track of these objects across frames. The primary goal is to create an efficient and real-time solution for vehicle detection and traffic monitoring.

## Features

- **Background Subtraction:** Uses the MOG2 algorithm to differentiate moving vehicles from the static background.
- **Object Tracking:** Employs Euclidean distance-based tracking to consistently identify and follow vehicles throughout the video.
- **Real-Time Processing:** Designed to handle video streams in real-time, making it suitable for live traffic monitoring applications.

## How It Works

1. **Video Capture:** The system reads the video feed from a specified file.
2. **Region of Interest (ROI):** A region of interest is defined to focus on the area where vehicles are expected to appear.
3. **Background Subtraction:** The `createBackgroundSubtractorMOG2` function is used to separate the moving objects (vehicles) from the background.
4. **Object Detection:** Contours are identified within the segmented foreground to detect vehicles.
5. **Object Tracking:** The detected vehicles are tracked using Euclidean distance, assigning a unique ID to each vehicle to maintain consistent tracking across frames.
6. **Counting:** The system counts the number of vehicles based on their unique IDs.

## Code Description

### Libraries Used

- **OpenCV:** Used for video capture, background subtraction, contour detection, and image processing.
- **tracker.py:** A custom Python script that implements the Euclidean distance tracking logic.

### Main Code

The core of the project involves:
- Capturing video frames and applying background subtraction.
- Detecting vehicle contours within the region of interest.
- Tracking detected vehicles using Euclidean distance.
- Displaying the results, including bounding boxes and IDs, on the video feed.

### Installation

To run this project, you need to have Python installed along with the following libraries:
```bash
pip install opencv-python
```

### Usage

1. Clone the repository.
2. Update the video file path in the script.
3. Run the script using Python.

```bash
python detect_track_count.py
```

### Results

The system displays the video feed with tracked vehicles highlighted by bounding boxes and IDs. The number of vehicles is counted in real-time.

## Conclusion

This project demonstrates the application of background subtraction and object tracking in real-world scenarios, such as traffic monitoring. It is a robust solution for detecting and counting vehicles in real-time, offering potential for further enhancements like speed estimation and multi-camera integration.

---
