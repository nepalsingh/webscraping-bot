import cv2 as cv
import os
from pathlib import Path

def grayscaler():

  files = os.listdir('images')
  print(files)

  for file in files:
      img = cv.imread(f'images/{file}')
      # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
      gray = cv.imread(f'images/{file}', 0)
      cv.imwrite(f'images/gray_to_{file}', gray)


def calculate_size(percent_change, width,height):
    width = int(percent_change * width / 100)
    height = int(percent_change * height / 100)
    return width, height

def resize_image(filepath,percent_change,resize_path):
    print(filepath,percent_change,resize_path)
    img = cv.imread(filepath)
    print(img.shape)
    width, height = calculate_size(percent_change, img.shape[1], img.shape[0])
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    cv.imwrite(resize_path, resized)

def resize_images():
    files = os.listdir('images')
    # files = Path('images')
    print(files)
    for file in files:
      if file.endswith('.jpeg'):
        resize_image(f'images/{file}', 20, f'images/resized/{file}')

if __name__ == '__main__':
    # grayscaler()
    resize_images()
