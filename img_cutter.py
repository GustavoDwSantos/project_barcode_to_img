import cv2

def calcula_contornos(img):
    contornos, hierarquia = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key = cv2.contourArea, reverse = True)[:10]
    return contornos

def img2recorte(contornos, img, prop_min, prop_max):
    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        proporcao = float(w)/h
        if proporcao >=prop_min and proporcao <=prop_max:
            etiqueta = img[y:y+h, x:x+w]
            return etiqueta
