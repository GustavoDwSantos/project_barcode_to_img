from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import requests
  

#Window setting
root = Tk()
root.title("Barcode Reader")
root.geometry("1400x800")
root.resizable(False, False)



#cam IP config
url = "http://192.168.0.102:8080/shot.jpg"
label = Label(root)
label.pack()




def show_frames():
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2imagem = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2imagem)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    label.after(10, show_frames)


#Button Setting
def Scan():
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2imagem = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


button = Button(root, text="Scan", command=Scan)
# button.grid(row=0, column=1)
button.pack()

show_frames()
root.mainloop()

