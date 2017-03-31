# this script is to convert a image form a photo to a paper like photo
import cv2
img=cv2.imread("IMG_20161222_115713_1.jpg")
# print(img)
# cv2.imshow("show",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
h=len(img)
w=len(img[0])
for x in range(h):
    for y in range(w):
        if max(img[x,y])- min(img[x,y]) <= 25:
            if max(img[x,y])>=150:
                img[x,y,0]=255
                img[x,y,1]=255
                img[x,y,2]=255
            else:
                img[x,y,0]=0
                img[x,y,1]=0
                img[x,y,2]=0
cv2.imwrite("atest12.jpg",img)
cv2.imshow("show",img)
cv2.waitKey(0)
cv2.destroyAllWindows()