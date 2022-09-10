#generate noise map
import numpy as np

def gaussian_noise(mean=0.,sigma=0.1,img_size=None):

    assert img_size,'argument:img_size can not be None'

    gaussian = np.random.normal(mean,sigma,img_size).astype(np.uint8)

    return gaussian
