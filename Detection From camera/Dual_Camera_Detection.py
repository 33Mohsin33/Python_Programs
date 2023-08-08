import cv2
import keyboard
def Camera():
    cam1=cv2.VideoCapture(0)
    cam2=cv2.VideoCapture(1)
    cv2.namedWindow("Computer Camera", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Flipped Camera", cv2.WINDOW_NORMAL)
    while(True):
        bool1,Frame1=cam1.read()
        Frame3=cv2.flip(Frame1,1)
        bool2,Frame2=cam2.read()
        cv2.imshow("Computer Camera",Frame1)
        cv2.waitKey(1)
        # cv2.imshow("Mobile Camera",Frame2)
        # cv2.waitKey(1)
        cv2.imshow("Flipped Camera",Frame3)
        cv2.waitKey(1)
        if(keyboard.is_pressed('q')):
         break
if(__name__=="__main__"):
    Camera()
