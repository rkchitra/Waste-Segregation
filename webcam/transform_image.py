import numpy as np
import cv2
import os

def transform(name) :
    width = 128
    height = 128
    dsize = (width,height)
    img = cv2.imread("pics_for_prediction/"+name,1)
    img2=cv2.resize(img,dsize)
    cv2.imwrite('pics_for_prediction/transformed'+name,img2)
    cv2.destroyAllWindows()
    return ('pics_for_prediction/transformed'+name)