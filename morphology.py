import cv2 as cv


img = cv.imread('lena.jpg')
element = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

erode_img = cv.erode(img, element)

dilate_img = cv.dilate(img,element)

cv.imshow('original',img)
cv.imshow('erode_img',erode_img)
cv.imshow('dilate_img',dilate_img)
cv.waitKey(0)

#other morphology operation:

#open:
open_img = cv.morphologyEx(img,cv.MORPH_OPEN,element)
cv.imshow('open',open_img)

#close:
close_img = cv.morphologyEx(img,cv.MORPH_CLOSE,element)
cv.imshow('close',close_img)

#grad:
grad_img = cv.morphologyEx(img,cv.MORPH_GRADIENT,element)
cv.imshow('grad',grad_img)

#tophat:
tophat_img = cv.morphologyEx(img,cv.MORPH_TOPHAT,element)
cv.imshow('tophat',tophat_img)

#backhat:
backhatp_img = cv.morphologyEx(img,cv.MORPH_BLACKHAT,element)
cv.imshow('backhat',backhatp_img)

cv.waitKey(0)
cv.destroyAllWindows()