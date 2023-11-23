import cv2
import imutils
import numpy as np
from imgTrat import imgTrat 
from imgTrat import elementos
import json

def carrega_img():
    # Carrega a imagem do campo
    image = cv2.imread('Campo.jpeg')
    # ajustando tamanho da imagem
    scale_percent = 30 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    #print(dim)
    # resize image
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    assert image is not None, "file could not be read, check with os.path.exists()"
    return image

# Carregando aquivo de imagem
img = carrega_img()
imTrat = imgTrat(img)
img = imTrat.img_ProjTransformation(img)
imagemTrat = imTrat.apply_brightness_contrast(img)
#imgTrat = imgTrat(img)
#img = imgTrat.img_ProjTransformation(img)
#imagemTrat = imgTrat.apply_brightness_contrast(img)
#hsv_image = cv2.cvtColor(imagemTrat, cv2.COLOR_BGR2HSV)

#mask = cv2.inRange(hsv_image, HSV_Min, HSV_Max)
#output = cv2.bitwise_and(imagemTrat, imagemTrat, mask = mask)
#Ball_Pos = imgTrat.obj_position(output)
ele = elementos(imagemTrat)
ballPose = ele.get_Ball_pos()
p1Pose = ele.get_Player_pos(img,0)
p2Pose = ele.get_Player_pos(img,1)
p3Pose = ele.get_Player_pos(img,2)
cv2.circle(img, ballPose, 7, (0, 0, 255), 2)
cv2.circle(img, np.int0([p1Pose[0], p1Pose[1]]), 15, (0, 0, 255), 2)
cv2.line(img,np.int0([p1Pose[0], p1Pose[1]]),
         np.int0([p1Pose[0]+10*np.sin(p1Pose[2]), p1Pose[1]+10*np.cos(p1Pose[2])]),(0, 0, 255),2)
cv2.circle(img, np.int0([p2Pose[0], p2Pose[1]]), 15, (0, 0, 255), 2)
cv2.line(img,np.int0([p2Pose[0], p2Pose[1]]),
         np.int0([p2Pose[0]+10*np.sin(p2Pose[2]), p2Pose[1]+10*np.cos(p2Pose[2])]),(0, 0, 255),2)
cv2.circle(img, np.int0([p3Pose[0], p3Pose[1]]), 15, (0, 0, 255), 2)
cv2.line(img,np.int0([p3Pose[0], p3Pose[1]]),
         np.int0([p3Pose[0]+10*np.sin(p3Pose[2]), p3Pose[1]+10*np.cos(p3Pose[2])]),(0, 0, 255),2)
cv2.imshow('a', img)
cv2.waitKey(0)