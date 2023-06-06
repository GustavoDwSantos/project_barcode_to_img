from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np

from img_url2cv2 import url2img
  
#Window setting
root = Tk()
root.title("Barcode Reader")
root.geometry("1350x800")
root.resizable(True, True)

#cam IP config
url = "http://192.168.0.100:8080/shot.jpg"
label = Label(root)
label.pack(side=LEFT)


image_return = Label(root)
image_return.pack(side=RIGHT)

#show frames camera
def show_frames():
    cv2imagem = url2img(url)
    img = Image.fromarray(cv2imagem)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    label.after(10, show_frames)

#Button comand
def Scan():
    img = url2img(url)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    image_return.imgtk = imgtk
    image_return.configure(image=imgtk)



#Button Setting
button = Button(root, text="Scan", command=Scan)
# button.grid(row=0, column=1)
button.pack(side=BOTTOM)

Scan()
show_frames()
root.mainloop()

