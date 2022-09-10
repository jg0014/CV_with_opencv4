# CV_with_opencv4
***
<font size=5>some computer vision implication with opencv4</font>

##environment<font size=4>
    python==3.6.13
    opencv-python==4.6.0

##</font>algorithm and usage
>###1.basic
> + <font size=4>1.1 Access an image: run read.py and save.py
> + 1.2 Encoding and Decoding: encoding.py and decoding.py. encoding an image as bytes flow

>###2.image transform
> + 2.1 Channel Split: channel_split&merge.py
> + 2.2 image flip: flip.py and rotate.py
> + 2.3 image concat: concat.py
> + 2.4 Extend border: padding.py
> + 2.5 high/low frequency filter: dft.py operate Discrete Fourier transform

>###3.image processing
> + 3.1 Color transform: color_trans.py
> + 3.2 Image morphology operator: morphology.py
> + 3.3 Image filtering: filters.py
> + 3.4 Histogram equalization: histogram.py

>###4.feature extraction
> + 4.1 Image thresholding: threshold.py including base thresholding and adaptive thresholding
> + 4.2 Image edge detection: edge_detection.py
> + 4.3 Image feature point detection: sift.py
> + 4.4 Dlob detection: blob.py
> + 4.5 Line and circle detection: Hough.py