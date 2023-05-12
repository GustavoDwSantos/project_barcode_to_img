from tkinter import *
from PIL import Image, ImageTk
import cv2

root = Tk()
root.title("Barcode Reader")
root.geometry("800x600")
root.resizable(False, False)

button = Button(root, text="Scan")
# button.grid(row=0, column=1)
button.pack()

label = Label(root)
# label.grid(row=0, column=0)
label.pack()
cap = cv2.VideoCapture(0)

def show_frames():
    cv2imagem = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2imagem)

    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    label.after(10, show_frames)

show_frames()
root.mainloop()

