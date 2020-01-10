import cv2

img = cv2.imread('src/Berry.jpg')

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

