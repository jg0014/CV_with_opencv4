import cv2 as cv

img = cv.imread('lena.jpg',cv.IMREAD_REDUCED_GRAYSCALE_2)

if img is None:
    print('Img Read Error!')
else:
    save_path='lena_reduce2.jpg'
    stat = cv.imwrite(filename=save_path,img=img)
#cv2.imwrite(filname,img,params)
#   filname: save path
#   img: target image
    if stat:
        print('Save image:{}'.format(save_path))