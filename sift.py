import numpy as np
import cv2


def load_image(path, gray=False):
    if gray:
        img = cv2.imread(path)
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        return cv2.imread(path)


def transform(origin):
    h, w, _ = origin.shape
    generate_img = np.zeros(origin.shape)
    for i in range(h):
        for j in range(w):
            generate_img[i, w - 1 - j] = origin[i, j]
    return generate_img.astype(np.uint8)


def main():
    img1 = load_image('lena.jpg')
    img2 = transform(img1)

    # 实例化
    sift = cv2.SIFT_create()

    # 计算关键点和描述子
    # 其中kp为关键点keypoints
    # des为描述子descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # 绘出关键点
    # 其中参数分别是源图像、关键点、输出图像、显示颜色
    img3 = cv2.drawKeypoints(img1, kp1, img1, color=(0, 255, 255))
    img4 = cv2.drawKeypoints(img2, kp2, img2, color=(0, 255, 255))

    # 参数设计和实例化
    index_params = dict(algorithm=1, trees=6)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # 利用knn计算两个描述子的匹配
    matche = flann.knnMatch(des1, des2, k=2)
    matchesMask = [[0, 0] for i in range(len(matche))]

    # 绘出匹配效果
    result = []
    for m, n in matche:
        if m.distance < 0.6 * n.distance:
            result.append([m])

    img5 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matche, None, flags=2)
    cv2.imshow("MatchResult", img5)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
    #img = cv2.imread('lena.jpg',0)


#from:https://zhuanlan.zhihu.com/p/70385018

#other feature detect:

def brisk_feature(img):
    assert len(img.shape)==2,'input image should be gray'

    brisk = cv2.BRISK_create()
    kpts = brisk.detect(img, None)

    img_keypoints = np.empty((img.shape[0], img.shape[1],3),dtype=np.uint8)
    cv2.drawKeypoints(img,kpts, img_keypoints)

    cv2.imshow('BRISK Keypoints', img_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def fast_feature(img):
    assert len(img.shape) == 2, 'input image should be gray'

    fast = cv2.FastFeatureDetector_create()
    kpts = fast.detect(img, None)

    img_keypoints = np.empty((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    cv2.drawKeypoints(img, kpts, img_keypoints)

    cv2.imshow('FAST Keypoints', img_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()