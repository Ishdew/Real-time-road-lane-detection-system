import cv2
import numpy as np

def threshold_rel(img, lo, hi):
    """ Applies a relative thresholding based on the min and max pixel values. """
    vmin = np.min(img)
    vmax = np.max(img)
    
    vlo = vmin + (vmax - vmin) * lo
    vhi = vmin + (vmax - vmin) * hi
    return np.uint8((img >= vlo) & (img <= vhi)) * 255

def threshold_abs(img, lo, hi):
    """ Applies an absolute thresholding based on fixed low and high values. """
    return np.uint8((img >= lo) & (img <= hi)) * 255

class Thresholding:

    def __init__(self):
        """ Init Thresholding."""
        pass

    def forward(self, img):
        """ Applies thresholding to the input image using HLS and HSV color spaces. """
        hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        h_channel = hls[:,:,0]
        l_channel = hls[:,:,1]
        s_channel = hls[:,:,2]
        v_channel = hsv[:,:,2]

        right_lane = threshold_rel(l_channel, 0.8, 1.0)
        right_lane[:,:750] = 0

        left_lane = threshold_abs(h_channel, 10, 100)
        left_lane &= threshold_rel(v_channel, 0.7, 1.0)
        left_lane[:,550:] = 0

        img2 = left_lane | right_lane

        return img2
