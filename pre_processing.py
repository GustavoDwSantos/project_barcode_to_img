import cv2
import numpy as np

def img2blackhat(img,kernel_tuple):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel_ret = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_tuple)
    black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_ret)
    return black_hat


def img2sobel(img,kernel_tuple):
    img = img2blackhat(img,kernel_tuple)
    sobel_y = cv2.Sobel(img, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = 1)
    sobel_y = np.absolute(sobel_y)
    sobel_y = sobel_y.astype('uint8')
    return sobel_y

def img2sobelblur(img,kernel_tuple):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_tuple)
    img = img2sobel(img,kernel_tuple)
    img = cv2.GaussianBlur(img,(5,5),0)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)
    return img

def limiar_otsu(img):
    valor, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    return img

def img2mask(img):
    kernel_quad = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fechamento = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel_quad)

    valor, mascara = cv2.threshold(fechamento, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return mascara

def aplica_masc(img,kernel_tuple):
    kernel_quad = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    img_blur = img2sobelblur(img,kernel_tuple)
    limiarizacao = limiar_otsu(img_blur)

    limiarizacao = cv2.erode(limiarizacao, kernel_quad, iterations = 2)
    limiarizacao = cv2.dilate(limiarizacao, kernel_quad, iterations = 2)

    mascara = img2mask(img)

    limiarizacao = cv2.bitwise_and(limiarizacao, limiarizacao, mask = mascara) 
    limiarizacao = cv2.dilate(limiarizacao, kernel_quad, iterations = 2)
    limiarizacao = cv2.erode(limiarizacao, kernel_quad)

    return limiarizacao

def upscale_x4(img):
    upscale = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "EDSR_x4.pb"
    upscale.readModel(path)
    upscale.serModel("edsr", 4)
    img_x4 = upscale.upsample(img)
    return img_x4





