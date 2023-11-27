import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tools import Tools as tl
import customtkinter as ctk


class Viewers:
    @classmethod
    def views(cls,u,inf):
        # main frame
        info = inf
        cls.u = u
        widt = 600
        hegt = 150

        # Create a photoimage object of the image in the path
        image1 = Image.open("C:/Users/ajuga/OneDrive/Desktop/test/nec3.jpg") #"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/images(book)/No Image/5.png"

        new_width  = 100
        new_height = 150
        img = image1.resize((new_width, new_height), Image.Resampling.LANCZOS)

        test = ImageTk.PhotoImage(img)
        r1 = ctk.CTkFrame(master=u,width= widt,height=hegt)

        r2 = ctk.CTkFrame(master=r1,width= 50,height=100, fg_color= "transparent")
        r2.pack(fill= "both", side= "left")

        divd = 1.2
        imgs = ctk.CTkImage(dark_image= img, size= (round(new_width/divd),round(new_height)/divd))
        cls.label1 = ctk.CTkLabel(master= r2,image=imgs,text= "")

        r4 = ctk.CTkFrame(r1,fg_color= "transparent")
        r4.pack(fill= "both",padx= 5,pady= 40, side= "top", anchor= tk.W)

        t = " "*53
        t2 = tl.inform(op="r")[1]
        t1 = tl.inform(op="r")[0].replace("-"," ").title()
        cls.lab1 = ctk.CTkLabel(r4,text= (f"{t1}"),
        font= ("TkDefaultFont",16),width= 480, anchor= "w",height= 18)
        cls.lab1.pack(fill= "x",padx= 5)

        ctk.CTkLabel(r4,text= (f"Author name".title()),
        font= ("TkDefaultFont",8),anchor= "w",height= 10).pack(fill= "x",padx= 5)

        cls.lab3 = ctk.CTkLabel(r4,text= (f"ʘ•Ongoing•{t2}".title()),
        font= ("TkDefaultFont",10),anchor= "w",height= 10)
        cls.lab3.pack(fill= "x",padx= 5)

        cls.label1.pack(padx= 5,pady=5,anchor='center')

        return r1
    
    @classmethod
    def update(cls,nam):
        inf = tl.inform(op="r")
        t = " "*(67-len(inf[0]))
        cls.lab1.configure(text = f"{inf[0]}{t}".title().replace("-"," "))
        cls.lab3.configure(text = f"ʘ•Ongoing•{inf[1]}.com{t}".title())

        image1 = Image.open(tl.img_read(nam))
        new_width  = 100
        new_height = 150
        img = image1.resize((new_width, new_height),  Image.Resampling.LANCZOS)
        divd = 1.2
        imgs = ctk.CTkImage(dark_image= img, size= (round(new_width/divd),round(new_height)/divd))
        cls.label1.configure(image=imgs)



