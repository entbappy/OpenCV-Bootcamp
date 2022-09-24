# import easyocr
import cv2


img = cv2.imread('Resources/bottle.jpg')
print(img.shape)
cv2.imshow('Output', img)
cv2.waitKey(0)
