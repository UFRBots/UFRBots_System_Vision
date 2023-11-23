import cv2
import json
import numpy as np
import elementos
from imgTrat import imgTrat

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

  

##############################################
# Limiarização bola
element = elementos.Ball()
def click_data_hsv(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
		#print(x, ' , ', y)
        h = hsv_image[y,x,0]
        s = hsv_image[y,x,1]
        v = hsv_image[y,x,2]
        text = str(h) + ',' + str(s) + ',' + str(v)
        element.limiarizacao.update(h,s,v)
        print("Parametros [h, s, v] atualizados")
        print("mínimo: " + str(element.limiarizacao.lim_min))
        print("máximo: " + str(element.limiarizacao.lim_max))

# Carregando aquivo de imagem
img = carrega_img()
imgTrat = imgTrat(img)
img = imgTrat.img_ProjTransformation(img)
imagemTrat = imgTrat.apply_brightness_contrast(img)
hsv_image = cv2.cvtColor(imagemTrat, cv2.COLOR_BGR2HSV)

while 1:
    mask = cv2.inRange(hsv_image, np.array(element.limiarizacao.lim_min,dtype=np.int32), np.array(element.limiarizacao.lim_max, dtype=np.int32))
    output = cv2.bitwise_and(imagemTrat, imagemTrat, mask = mask)
    cv2.imshow("images", np.hstack([imagemTrat, output]))
    cv2.setMouseCallback('images', click_data_hsv)
    k = cv2.waitKey(0)
    if k == 27: break
cv2.destroyAllWindows() # fechando todas as janelas
# implode e explode para eliminar ruidos 
#output = cv2.resize(output, (6*13,6*15), interpolation = cv2.INTER_AREA)
#output = cv2.resize(output, (3*130,3*150), interpolation = cv2.INTER_AREA)
output= cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
(thresh, output) = cv2.threshold(output, 50, 255, cv2.THRESH_BINARY)
#[Ball_x, Ball_y] = centroide(output)
#cv2.circle(imagemTrat, (Ball_x, Ball_y), 10, (0, 0,255),1)
cv2.imshow('a', output)
cv2.waitKey(0)