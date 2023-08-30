import cv2 as cv

# Read the video
capture = cv.VideoCapture('video.mp4')
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
fps = int(capture.get(cv.CAP_PROP_FPS))
print(width, height, frames, fps)
