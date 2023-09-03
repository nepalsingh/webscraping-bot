import cv2 as cv

# Read the video
capture = cv.VideoCapture(1)
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
fps = int(capture.get(cv.CAP_PROP_FPS))
print(width, height, frames, fps)
success, frame = capture.read()

while success:
    success, frame = capture.read()
    cv.imshow('Recording', frame)
    key = cv.waitKey(20)
    if key == ord('q'):
        break
