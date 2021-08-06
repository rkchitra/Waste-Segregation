import numpy as np
import cv2
import os
def transform(name):
    width = 128
    height = 128
    x = 320-80
    y = 170
    h = 150
    w = 150
    img = cv2.imread("static/pics_for_prediction/"+name,1)
    crop_img = img[y:y+h, x:x+w]
    dsize = (width,height)
    img2=cv2.resize(crop_img,dsize)
    cv2.imwrite('static/pics_for_prediction/transformed'+name,img2)
    return ('static/pics_for_prediction/transformed'+name)

def transform2(name) : 
    width = 128
    height = 128
    img = cv2.imread("static/pics_for_prediction/"+name,1)
    dsize = (width,height)
    img2 = cv2.resize(img,dsize)
    cv2.imwrite('static/pics_for_prediction/transformed'+name,img2)
    return ('static/pics_for_prediction/transformed'+name)



