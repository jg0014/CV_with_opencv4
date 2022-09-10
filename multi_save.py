import cv2 as cv

img1 = cv.imread('lena.jpg')
img2 = cv.imread('lena_reduce2.jpg')
img = [img1,img2]

save_path = 'multi_lena.tiff'
stat = cv.imwritemulti(save_path,img)
if stat:
    print('Save image:{}'.format(save_path))