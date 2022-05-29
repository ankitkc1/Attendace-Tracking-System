import cv2
from time import sleep
webcam = cv2.VideoCapture(0)
#function to capture the photo of new person and saving in images folder
def SetData(x):
    while True:
        try:
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                f =  x +".jpg"
                path = "./images/" + f
                cv2.imwrite(filename=path, img=frame)
                webcam.release()
                img_ = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
                break    
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
        
        except(KeyboardInterrupt):
            webcam.release()
            cv2.destroyAllWindows()
            break