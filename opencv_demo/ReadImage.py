# __*__ coding: utf-8 __*__
"""
Created on 2018.2.5
@auther:bnhc

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read file for disk
img = cv2.imread("/home/bnhc/PycharmProjects/Hello_World_Python/opencv_demo/test.jpg", 0)

# show file use window

# cv2.imshow("image",img)
# # cv2.waitKey() KeyWord KeyEvent
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Anther Method show Image: Create Window First And Full into Image

# cv2.namedWindow("bnhc",cv2.WINDOW_GUI_EXPANDED)
# cv2.imshow("bnhc",img)
# cv2.waitKey(0)
# cv2.imwrite("/home/bnhc/PycharmProjects/Hello_World_Python/opencv_demo/HelloWorld.jpg",img)
# cv2.destroyAllWindows();

# Loading a gray Image And Show. It's will save local When press "s" key And exit with "ESC"

# cv2.imshow("bnhc", img)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:  # wait for ESC to Exit
#     cv2.destroyAllWindows()
# elif k == ord('s'):  # Wait for s to save file
#     cv2.imwrite("/home/bnhc/PycharmProjects/Hello_World_Python/opencv_demo/helloWorld.png", img)
#     cv2.destroyAllWindows()

"""
    Matplotlib library
"""
plt.imshow("bnhc",img)
plt.xticks(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([]) # to hide tick values on X and Y axi
plt.show()