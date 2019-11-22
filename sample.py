import cv2

img = cv2.imread("assets/imori.jpg")

img3 = img.copy()

H, W, C = img3.shape

img3[:H//2, :W//2] = img3[:H//2, :W//2, (2,1,0)]

cv2.imshow('',img3)


cv2.waitKey(0)
cv2.destroyAllWindows()