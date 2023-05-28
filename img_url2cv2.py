import requests
import numpy as np
import cv2


def url2cv2(url):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return cv2img
