import numpy as np
import cv2 as cv

#discrete fourier transform for image
img = cv.imread('lena.jpg',0)
img_fc1 = np.float32(img)
#dft
dft_img = cv.dft(img_fc1,flags=cv.DFT_COMPLEX_OUTPUT)

#Transfer the low-frequency part of the transformed image to the center of the image
dft_center = np.fft.fftshift(dft_img)

#Convert real part and complex part to real part and normalize
temp=np.array([])
result = np.log(np.abs(cv.magnitude(dft_center[:, :, 0], dft_center[:, :, 1])))
result = cv.normalize(result,temp,norm_type=cv.NORM_MINMAX)

#Set the low frequency area to 0:High pass filtering
highpass = dft_center.copy()
highpass[200:311,200:311]=0
dft_icenter = np.fft.ifftshift(highpass)#dft_center
hp_reconstruct = cv.idft(dft_icenter)
hp_reconstruct = cv.magnitude(hp_reconstruct[:, :, 0], hp_reconstruct[:, :, 1])
temp2=np.array([])
hp_reconstruct = cv.normalize(hp_reconstruct,temp2,norm_type=cv.NORM_MINMAX)

#Set the high frequency area to 0:low pass filtering
lowpass = dft_img.copy()
lowpass[50:461,50:461]=0
lp_reconstruct = cv.idft(lowpass)
lp_reconstruct = cv.magnitude(lp_reconstruct[:, :, 0], lp_reconstruct[:, :, 1])
temp3=np.array([])
lp_reconstruct = cv.normalize(lp_reconstruct,temp3,norm_type=cv.NORM_MINMAX)

#if (cv.compare(img,lp_reconstruct,cv.CMP_EQ)):
#    print('EQ')
cv.imshow('original',img)
cv.imshow('dft_img',result)
cv.imshow('hp_rec',hp_reconstruct)
cv.imshow('lp_rec',lp_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()

