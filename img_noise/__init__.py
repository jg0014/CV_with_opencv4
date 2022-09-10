import numpy as np
import cv2 as cv

class add_noise():

    def __init__(self,range_value=(0,255)):
        super(add_noise, self).__init__()
        self.max_value = range_value[1]
        self.min_value = range_value[0]

    def add_noise(self,img,noise_map):
        noise_img = img+noise_map
        noise_img = np.clip(noise_img,a_min=self.min_value,a_max=self.max_value)

        return noise_img