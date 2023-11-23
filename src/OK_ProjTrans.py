import cv2
import json
import numpy as np
import matplotlib.pyplot as plt

# Coordenadas do Campo 
campo_dim=[[0,0],[3*130,0],[3*130,3*150],[0, 3*150]]

# Função que pega as coordenadas dos vertices co campo para correção de pespectiva
def click_data(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        #print(x, ' , ', y)
        cv2.polylines(img, [coords], False  , (255,0,0),2)
        if x < cols/2 and y < rows/2: coords[0] = [x,y]
        if x > cols/2 and y < rows/2: coords[1] = [x,y]
        if x < cols/2 and y > rows/2: coords[3] = [x,y]
        if x > cols/2 and y > rows/2: coords[2] = [x,y]
        
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

# Inicia a matriz de pespectiva
imagem = carrega_img()
img = imagem

rows,cols,ch = img.shape
coords = np.array([[56,65],[368,52],[389,390],[28,387]])
while(1):
    pts1 = np.float32()
    img = carrega_img()
    cv2.polylines(img, [coords], True, (255,0,0),2)
    cv2.imshow("ORIGINAL",img)
    cv2.setMouseCallback("ORIGINAL", click_data)
    k = cv2.waitKey(0)
    if k == 27:
        lists = coords.tolist()
        json_str = json.dumps(lists)
        print("\"ProjTransfCoords\" :" + json_str+",") 
        #      str(coords[1,1])+","+ str(coords[1,2])+",") 
        break
    
pts1 = np.float32(coords)
pts2 = np.float32(campo_dim)
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(imagem,M,(3*130, 3*150))
cv2.imshow("OUTPUT", dst)
cv2.waitKey(0)