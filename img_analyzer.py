import pytesseract as tess
import cv2
from pytesseract import Output
from pyzbar.pyzbar import decode, ZBarSymbol

from img_cutter import calcula_contornos
from pre_processing import aplica_masc


def img_dict(img):
    config_tesseract = "--tessdata-dir tessdata --psm 3"
    dict_img = tess.image_to_data(img, output_type=Output.DICT, lang='por', config=config_tesseract)
    return dict_img


def caixa_texto(img ,cor = (225, 100, 0)):
  img_masc = aplica_masc(img, kernel_tuple=(10,25))
  contornos = calcula_contornos(img_masc)
  for contorno in contornos:
      x, y, w, h = cv2.boundingRect(contorno)
      proporcao = float(w)/h
      if proporcao >=0.1 and proporcao <=0.9:
          cv2.rectangle(img,(x,y), (x+w ,y + h), cor , 2 )
          return img
  return img
      

def barcode_reader_img(etq):  
  data = decode(etq, symbols=ZBarSymbol)
  if len(data) > 0:
    return data[0][0]
  else:pass

