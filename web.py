import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tools import Tools as tl
import customtkinter as ctk


class Webp():
    webs = []
    typp = 0
    ope = False
    def __init__(self,r,nam= "NovelHard",url="C:/Users/ajuga/OneDrive/Desktop/test/clas_4.jpg",
    txt="Sample scrolling label, labels",ev1= "",ev2= "",ev3= "", typ= 0, g= "") -> None:
        self.typ = typ
        self.ev1 = ev1
        self.ev2 = ev2
        self.ev3 = ev3
        self.g = g
        image1 = Image.open(url)
        new_width  = 100
        new_height = 70
        #img = image1.resize((new_width, new_height), Image.Resampling.LANCZOS)
        #test = ImageTk.PhotoImage(img)

        self.web = len(self.webs)
        self.webs.append(self.web)
        s = ttk.Style()
        s.configure('red.TFrame', background='white')
        #ctk.can

        l2 = ctk.CTkFrame(r, fg_color= "transparent")
        divd = 0.6
        imgs = ctk.CTkImage(dark_image= image1, size= (round(new_width/divd),round(new_height)/divd))
        label1 = ctk.CTkLabel(l2,image=imgs,text=nam,compound= "top", fg_color= "#999999")
        #label1.image = test
        label1.pack(side="left",anchor="w")
        label1.bind("<Button-1>",self.click)
        #ctk.CTkLabel(l2, text=txt).pack(side= "left",anchor= "s", padx = 5)
    
    def click(self,event):
        if self.ev1 != "":
            self.typp = self.typ
            self.ev1.lift()
            #print(self.typp)
            self.g(self.typp)

    