#image edge detection
import cv2 as cv

img = cv.imread('lena.jpg',0)

#Sobel edge detection:
sobel_x = cv.Sobel(img,ddepth=-1,dx=1,dy=0)

sobel_y = cv.Sobel(img,ddepth=-1,dx=0,dy=1)

sobel_grad = cv.addWeighted(src1=sobel_x,alpha=0.5,src2=sobel_y,beta=0.5,gamma=0)

sobel_grad_=cv.Sobel(img,ddepth=-1,dx=1,dy=1)

cv.imshow('grad_x',sobel_x)
cv.imshow('grad_y',sobel_y)
cv.imshow('grad_x_y',sobel_grad)
cv.imshow('grad_xy',sobel_grad_)

cv.waitKey(0)
cv.destroyAllWindows()

#Scharr edge detection:
scharr_x = cv.Scharr(img,ddepth=-1,dx=1,dy=0)

scharr_y = cv.Scharr(img,ddepth=-1,dx=0,dy=1)

scharr_grad = cv.addWeighted(src1=sobel_x,alpha=0.5,src2=sobel_y,beta=0.5,gamma=0)

#scharr_grad_=cv.Scharr(img,ddepth=-1,dx=1,dy=1)

cv.imshow('grad_x',scharr_x)
cv.imshow('grad_y',scharr_y)
cv.imshow('grad_x_y',scharr_grad)
#cv.imshow('grad_xy',scharr_grad_)

cv.waitKey(0)
cv.destroyAllWindows()

#Laplancian:
laplancian_grad = cv.Laplacian(img,-1)
cv.imshow('laplancian',laplancian_grad)

cv.waitKey(0)
cv.destroyAllWindows()

#Canny edge detection:
canny_grad = cv.Canny(img,70,160)

cv.imshow('canny',canny_grad)
cv.waitKey(0)
cv.destroyAllWindows()