import cv2 as cv
import os


def detect_face(image_path):
    face_cascade = cv.CascadeClassifier('faces.xml')
    img = cv.imread(image_path,1)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    # print(faces)
    print(f'{image_path}')
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)
    cv.imwrite(f'{image_path}', img)

def batch_detect_face():
  images_folder = 'images/faces'
  for file in os.listdir(images_folder):
      if file.endswith('.jpeg'):
          print('file',file)
          detect_face(f'{images_folder}/{file}')

if __name__ == '__main__':
    batch_detect_face()