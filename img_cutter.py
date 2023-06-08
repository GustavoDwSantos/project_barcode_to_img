import cv2
from pre_processing import *

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
        

def img2recorte_barcode(contornos, img, prop_min, prop_max):
    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        proporcao = float(w)/h
        if proporcao >=prop_min and proporcao <= prop_max:
            barcode = img[0:-1, x:x+w]
            planilha = img[0:-1, 0:x]
            return barcode, planilha

def img2etq(img):
    img_transformed = aplica_masc(img, kernel_tuple=(10,25))
    etq = img2recorte(calcula_contornos(img_transformed), img, 0.1, 0.9)
    return etq

def etqextractbarcode(img):
    kernel_quad = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    etq = img2etq(img)
    img_blur = img2sobelblur(etq, kernel_tuple=(1,6))
    limiarizacao = limiar_otsu(img_blur)

    limiarizacao = cv2.erode(limiarizacao, kernel_quad, iterations = 2)
    limiarizacao = cv2.dilate(limiarizacao, kernel_quad, iterations = 3)
    barcode, planilha = img2recorte_barcode(calcula_contornos(limiarizacao), etq, 0.1, 0.9)
    return barcode ,planilha