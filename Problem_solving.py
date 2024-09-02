import cv2
from tracker import *

tracker = EuclideanDistTracker()
cap = cv2.VideoCapture(r'D:\Courses language programming\7_Computer Vision\Computer Vision - Full Course\6-Object Detection\detect-track-and-count-car-and-moto-in-video-using-openCV-main\highway.mp4')
object_detector = cv2.createBackgroundSubtractorMOG2(history=1000, varThreshold=50)

while True:
    ret, image = cap.read()
    if not ret:
        break
    h, w, _ = image.shape
    roi = image[340:720, 500:800]

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detector = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            x, y, w, h = cv2.boundingRect(contour)
            detector.append([x, y, w, h])



    boxes_id = tracker.update(detector)
    for box_id in boxes_id:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y), cv2.FONT_ITALIC, 1, (0, 0, 255), 1)
        cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 1)

    cv2.imshow('image', image)
    cv2.imshow('roi', roi)
    cv2.imshow('mask', mask)

    if cv2.waitKey(30) == ord('o'):
        break

cv2.destroyAllWindows()
cap.release()
