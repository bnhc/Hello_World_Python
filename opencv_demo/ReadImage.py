# __*__ coding: utf-8 __*__
"""
Created on 2018.2.5
@auther:bnhc

"""
import numpy as np
import cv2

# read file for disk
img = cv2.imread("girl.jpg",0)

# show file use window

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


