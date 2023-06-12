import pytesseract as tess
import cv2
from pytesseract import Output
from pyzbar.pyzbar import decode, ZBarSymbol


def img_dict(img):
    config_tesseract = "--tessdata-dir tessdata --psm 3"
    dict_img = tess.image_to_data(img, output_type=Output.DICT, lang='por', config=config_tesseract)
    return dict_img


def caixa_texto(dict_img, img ,cor = (225, 100, 0)):
  x = dict_img['left'][i]
  y = dict_img['top'][i]
  w = dict_img['width'][i]
  h = dict_img['height'][i]
 
  cv2.rectangle(img,(x,y), (x+w ,y + h), cor , 2 )
  
  return x, y, img

def barcode_reader_img(etq):  
  data = decode(etq, symbols=ZBarSymbol)
  if len(data) > 0:
    return data[0][0]
  else:pass

