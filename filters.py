import cv2 as cv
from img_noise.noise import gaussian_noise
import img_noise

org_img = cv.imread('lena.jpg',0)

cv.imshow('original',org_img)

noise_map = gaussian_noise(mean=0,sigma=11,img_size=org_img.shape)
img = img_noise.add_noise(range_value=[0,255]).add_noise(img=org_img,noise_map=noise_map)

cv.imshow('noise_img',img)

box_filter = cv.boxFilter(img,ddepth=-1,ksize=(3,3))
cv.imshow('box_filter',box_filter)

mean_filter = cv.blur(img,(3,3))
cv.imshow('mean_filter',mean_filter)

gaussian_img = cv.GaussianBlur(src=img,ksize=(3,3),sigmaX=11,sigmaY=11)
cv.imshow('gaussian',gaussian_img)

bilateral_img = cv.bilateralFilter(img,d=5,sigmaColor=25,sigmaSpace=25)
cv.imshow('bilateral',bilateral_img)

median_img = cv.medianBlur(img,ksize=3)
cv.imshow('median',median_img)

cv.waitKey(0)
cv.destroyAllWindows()