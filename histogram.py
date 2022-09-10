import numpy as np
import cv2 as cv

img = cv.imread('lena.jpg',0)

def hist_img(hist):
    minVal, maxVal, minLoc, maxLoc= cv.minMaxLoc(hist)
    hist_image = np.zeros([256,256],np.uint8)
    hist_image[:]=255
    #draw hist:
    for i in range(256):
        norm_value = int(hist[i]*256/maxVal)
        cv.line(hist_image,(i,256),(i,256-norm_value),[0,0,0])
    return hist_image

#***—————————————————————————————————split———————————————————————————————————***#

hist = cv.calcHist(images=[img], channels=[0],mask=None,histSize=[256],ranges=[0,255])

hist_image = hist_img(hist)
cv.imshow('hist_image',hist_image)
cv.imshow('origin_img',img)

equalize_img = cv.equalizeHist(img)
equalize_hist = cv.calcHist([equalize_img],channels=[0],mask=None,histSize=[256],ranges=[0,255])
equalize_hist_img = hist_img(equalize_hist)
cv.imshow('equalized_img',equalize_img)
cv.imshow('equalized_hist',equalize_hist_img)

cv.waitKey(0)
cv.destroyAllWindows()