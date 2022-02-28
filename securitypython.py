import cv2
import dropbox
import random
import time

def take_snapshot():
  print("Went into snapshot function")
  cv = cv2.VideoCapture(0)
  res = True
  imageName = "img" + str(random.randint(1,100)) + ".png"
  while(res):
    result, frame = cv.read()
    cv.imwrite(imageName, frame)
    res = False
  print("Snapshot taken")
  cv.release()
  cv2.destroyAllWindows()
  return imageName

def upload(imgName):
  dest = "/Home/Demo/" + imgName
  access_token = "J9C94Tww7TcAAAAAAAAAATmzk1OsvHjudHpyGzS5wseDI6p3QiEtYKBQdiG2muVe"
  db = dropbox.Dropbox(access_token)

  f = open(imgName, "rb")
  db.files_upload(f.read(), dest)
def main():
  startTime = time.time();
  while(True):
    currTime = time.time();
    if currTime - startTime > 5:
      upload(take_snapshot())
main()
