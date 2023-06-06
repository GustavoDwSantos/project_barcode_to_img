import cv2
import numpy as np

def img2blackhat(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel_ret = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_ret)
    return black_hat


def blackhat2sobel(img):
    img = img2blackhat(img)
    sobel_x = cv2.Sobel(img, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = 1)
    sobel_x = np.absolute(sobel_x)
    sobel_x = sobel_x.astype('uint8')
    return sobel_x

def aplica_masc(img):
    kernel_ret = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    kernel_quad = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))


    img_sobel = blackhat2sobel(img)
    img_sobel = cv2.GaussianBlur(img_sobel, (5,5), 0)
    img_sobel = cv2.morphologyEx(img_sobel, cv2.MORPH_CLOSE, kernel_ret)

    valor, limiarizacao = cv2.threshold(img_sobel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    limiarizacao = cv2.erode(limiarizacao, kernel_quad, iterations = 2)
    limiarizacao = cv2.dilate(limiarizacao, kernel_quad, iterations = 2)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fechamento = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel_quad)

    valor, mascara = cv2.threshold(fechamento, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    limiarizacao = cv2.bitwise_and(limiarizacao, limiarizacao, mask = mascara) 
    limiarizacao = cv2.dilate(limiarizacao, kernel_quad, iterations = 2)
    limiarizacao = cv2.erode(limiarizacao, kernel_quad)

    return limiarizacao

def calcula_contornos(img):
    img = aplica_masc(img)
    contornos, hierarquia = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key = cv2.contourArea, reverse = True)[:10]
    return contornos

        





