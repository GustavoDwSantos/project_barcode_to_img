from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np

from img_url2cv2 import url2img
  
#Window setting
root = Tk()
root.title("Barcode Reader")
root.geometry("1400x800")
root.resizable(False, False)

#cam IP config
url = "http://192.168.0.102:8080/shot.jpg"
label = Label(root)
label.pack()

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
    cv2imagem = url2img(url)

#Button Setting
button = Button(root, text="Scan", command=Scan)
# button.grid(row=0, column=1)
button.pack()

show_frames()
root.mainloop()

