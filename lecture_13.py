import cv2

img = cv2.imread('src/grapes.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

print(img_gray.shape)
print(img_hsv.shape)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_gray2 = cv2.imread('src/grapes.jpg', 0)

cv2.imshow('gray', img_gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img_hsv)

