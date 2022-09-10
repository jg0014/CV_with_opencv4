import cv2
import numpy as np

params = cv2.SimpleBlobDetector_Params()

# 设置阈值
params.minThreshold = 10
params.maxThreshold = 200
# 设置选择区域
params.filterByArea = True
params.minArea = 1500
# 设置圆度
params.filterByCircularity = True
params.minCircularity = 0.1
# 设置凸度
params.filterByConvexity = True
params.minConvexity = 0.87
# 设置惯性比
params.filterByInertia = True
params.minInertiaRatio = 0.01

im = cv2.imread("blob_detection.jpg", cv2.IMREAD_GRAYSCALE)
detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(im)
with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]),(0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", with_keypoints)
cv2.waitKey(0)