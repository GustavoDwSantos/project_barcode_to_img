from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
from img_analyzer import *
from img_cutter import *

from img_url2cv2 import *
from pre_processing import *
  
class EtqFounder(Frame):

    def __init__(self, master, scanframe, img):
        super().__init__(master)
        
        options = {'padx': 5, 'pady': 5}

        self.img = img
        self.img_resize = cv2.resize(self.img, (0,0), fx=0.5, fy=0.5)
        self.img_resize = Image.fromarray(self.img_resize)
        self.img_resize = ImageTk.PhotoImage(image=self.img_resize)
        self.label_img = Label(self, image =self.img_resize)
        self.label_img.grid(row=0, column=0, **options)

        self.label_message = Label(self, text="Imagem Encontrada, deseja fazer o processo de OCR?")
        self.label_message.grid(row=1, column=0, columnspan= 2, **options)

        self.button_yes = Button(self, text="Sim", command=self.yes)
        self.button_yes.grid(row=2, column=0,**options)

        self.button_no = Button(self, text="Não", command=self.no)
        self.button_no.grid(row=2, column=1, **options)

        self.scanframe = scanframe

        self.grid(padx=10, pady=10, sticky=NSEW)

        

    def yes(self):
        dict_img = cutdata2etq(self.img)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,5))
        self.scanframe.process_image_line(dict_img, "lote", self.scanframe.lote_var, kernel)
        self.scanframe.process_image_line(dict_img, "nom_wt", self.scanframe.nom_wt_var, kernel)
        self.scanframe.process_image_line(dict_img, "units", self.scanframe.units_var, kernel)
        self.scanframe.process_image_line(dict_img, "net", self.scanframe.net_var, kernel)
        self.scanframe.process_image_line(dict_img, "set", self.scanframe.set_var, kernel)
        self.scanframe.process_image_line(dict_img, "pkg", self.scanframe.pkg_var, kernel)
        self.master.destroy()

    def no(self):
        self.ocr = False
        self.master.destroy()



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
        self.button = Button(self, text="Scan", command=self.scan)
        self.button.grid(row=7, column=1, columnspan=2, **options)

        self.show_frames()

        self.grid(padx=10, pady=10, sticky=NSEW)
    
    def show_frames(self):
        cv2imagem = url2img(self.url)
        img_box = caixa_texto(cv2imagem)
        if len(img_box) > 0:
            img = Image.fromarray(img_box)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label_cam.imgtk = imgtk
            self.label_cam.configure(image=imgtk)
        else:
            img = Image.fromarray(cv2imagem)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label_cam.imgtk = imgtk
            self.label_cam.configure(image=imgtk)

        self.label_cam.after(10, self.show_frames)
    
    def process_image_line(self ,dict_img, key, variable, kernel):
        
        img = upscale_x4(dict_img[key])
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        limiar = limiar_otsu(gray)
        fechamento = cv2.morphologyEx(limiar, cv2.MORPH_CLOSE, kernel)
        data = img_dict(fechamento)

        for string in data['text']:
            if string and len(string) > len(variable.get()):
                variable.set(string)


    def scan(self):
        img = url2img(self.url)
        etq = img2etq(img)
        app2 = Message()
        frame2 = EtqFounder(app2, self, etq)
        app2.mainloop()

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Barcode Reader")
        self.geometry("900x560")
        self.resizable(True, True)

class Message(Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Etiqueta Encontrada")
        self.geometry("400x600")
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    frame = ScanFrame(app)
    app.mainloop()


