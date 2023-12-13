import cv2
image=cv2.imread("lena.jpg",1)
cv2.line(image,(0,0),(560,560),(250,0,0),3)
cv2.circle(image,(70,70),70,(0,0,255),-1)
cv2.circle(image,(440,440),70,(0,0,255),-1)
cv2.circle(image,(70,-70),70,(0,0,255),-1)
cv2.rectangle(image,(160,160),(350,350),(0,255,0),4)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"HEY",(190,250),font,2,(10,56,167))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()