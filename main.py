from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
from img_analyzer import barcode_reader_img, caixa_texto
from img_cutter import img2etq

from img_url2cv2 import url2img
  


class ScanFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        options = {'padx': 5, 'pady': 5}

        #cam IP config
        self.url = "http://192.168.0.101:8080/shot.jpg"
        self.label_cam = Label(self)
        self.label_cam.grid(row=1, rowspan=7, column=0, **options)

        
        """self.image_return = Label(self)
        self.image_return.grid(row=1, column=2, **options)"""

        # Entry Setting
        self.lote_var = StringVar()
        self.nom_wt_var = StringVar()
        self.units_var = StringVar()
        self.net_var = StringVar()
        self.set_var = StringVar()
        self.pkg_var = StringVar()

        self.entries = [
            ("Lote", self.lote_var),
            ("NOM.WT", self.nom_wt_var),
            ("UNITS", self.units_var),
            ("NET", self.net_var),
            ("SET", self.set_var),
            ("PKG", self.pkg_var),
        ]

        for i, (label_text, var) in enumerate(self.entries):
            self.label = Label(self, text=label_text)
            self.label.grid(row=i+1, column=1, **options)
            self.entry = Entry(self, textvariable=var, state="disabled")
            self.entry.grid(row=i+1, column=2, **options)

        #Button Setting
        self.button = Button(self, text="Scan", command=self.Scan)
        self.button.grid(row=7, column=1, columnspan=2, **options)

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
        etq = img2etq(img)
        barcode = barcode_reader_img(etq)
        print(barcode)
        self.pkg_var.set(barcode)
        

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Barcode Reader")
        self.geometry("900x560")
        self.resizable(True, True)


if __name__ == "__main__":
    app = App()
    frame = ScanFrame(app)
    app.mainloop()


