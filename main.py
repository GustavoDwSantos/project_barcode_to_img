from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np

from img_url2cv2 import url2img
  


class ScanFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        options = {'padx': 5, 'pady': 5}

        #cam IP config
        self.url = "http://192.168.0.101:8080/shot.jpg"
        self.label_cam = Label(self)
        self.label_cam.grid(row=1, column=0, **options)

        
        self.image_return = Label(self)
        self.image_return.grid(row=1, column=2, **options)

        #Button Setting
        self.button = Button(self, text="Scan", command=self.Scan)
        self.button.grid(row=2, column=1, **options)

        self.show_frames()

        self.grid(padx=10, pady=10, sticky=NSEW)
    
    def show_frames(self):
        cv2imagem = url2img(self.url)
        img = Image.fromarray(cv2imagem)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label_cam.imgtk = imgtk
        self.label_cam.configure(image=imgtk)

        self.label_cam.after(10, self.show_frames)
    
    def Scan(self):
        img = url2img(self.url)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.image_return.imgtk = imgtk
        self.image_return.configure(image=imgtk)

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Barcode Reader")
        self.geometry("1350x800")
        self.resizable(True, True)


if __name__ == "__main__":
    app = App()
    frame = ScanFrame(app)
    app.mainloop()


