import cv2

#画像を読み込んで、RGBをBGRに変える
img = cv2.imread("imori.jpg")

img2 = img[:,:,(2,1,0)]

cv2.imshow("" , img2)


cv2.waitKey(0)
cv2.destroyAllWindows()