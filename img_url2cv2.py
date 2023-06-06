import requests
import numpy as np
import cv2


def url2img(url):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
