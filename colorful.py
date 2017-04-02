import cv2
import numpy as np

def returncolor():
    r=np.random.randint(0,255)
    g=np.random.randint(0,255)
    if r+g<100:
        start=100-r-g
    else:
        start=np.uint8(0)
    if r+g>410:
        end=255+480-r-g
    else:
        end=255
    if end<=start:
        end=start
    b=np.random.randint(start,end)
    return np.uint8(r),np.uint8(g),np.uint8(b)
def generatecolor(img):
    long=img.shape[0]*img.shape[1]
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            r,g,b=returncolor()
            img[x][y][0]=r
            img[x][y][1]=g
            img[x][y][2]=b


img=np.zeros((1080,1920,3),np.uint8)
generatecolor(img)
cv2.imwrite("test.jpg",img)