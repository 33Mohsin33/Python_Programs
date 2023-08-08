import cv2
import keyboard
def face_Det():
    Face= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    cam=cv2.VideoCapture(0)
    while(True):
        boool,frame=cam.read()
        frame=cv2.flip(frame,1)
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera",frame)
        cv2.waitKey(1)
        if(keyboard.is_pressed('q')):
         break
if (__name__=="__main__"):
 face_Det()
