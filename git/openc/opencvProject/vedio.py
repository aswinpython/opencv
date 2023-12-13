import cv2
capture=cv2.VideoCapture(0)
while(True):
    rest,frame=capture.read(0)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',grey)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
capture.release()
cv2.destroyAllWindows()