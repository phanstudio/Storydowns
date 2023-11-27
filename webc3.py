
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Webp2():
    def __init__(self,r,nam= "I hate systems",url="C:/Users/ajuga/OneDrive/Desktop/test/clas_4.jpg") -> None:

        image1 = Image.open(url)
        new_width  = 100
        new_height = 70
        img = image1.resize((new_width, new_height), Image.Resampling.LANCZOS)
        test = ImageTk.PhotoImage(img)

        s = ttk.Style()
        s.configure('red.TFrame', background='white')

        l2 = ttk.Frame(r,padding=5)
        label1 = ttk.Label(l2,image=test,text=nam,compound= "top", style= "red.TButton")
        label1.image = test
        label1.pack(side="left")