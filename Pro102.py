import cv2
import dropbox
import time 
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()

        #cv2.imwrite() is used to save an image to any storage device
        img_name = 'img' + str(number) + '.png'
        cv2.imwrite(img_name, frame)
        start_time = time.time
        
        result = False
    
    return img_name
    print('Snapshot taken')

    #release the camera
    videoCaptureObject.release()

    #close all the windows that might be opened by the camera
    cv2.destroyAllWindows()

def upload_file(img_name):
      access_token = 'sl.A8wVcO-WRe45FBcwRKMWK-qNPOhWRX8E0zXNDxSTKiu-rpc3TC-Kzu7POqnBK_WZ4glZeaXhyP3kKx0BQcBNkT9XiKbrnFMFSbre_vrHgfOymTfBGcrTQFx5HAN5b0FL4xf6Jr8'
      file = img_name
      file_from = file
      file_to = '/NewFolder/' + (img_name)
      dbx = dropbox.Dropbox(access_token)

      with open(file_from,'rb') as f:
          dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
          print('File Uploaded')

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)

#call the function
main()


