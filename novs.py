import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random as rd
from tools import Tools as tl
import customtkinter as ctk



class Novel():
    op = False
    def __init__(self,r,num=0,nam= "NovelHard",u= "",
    txt="Sample scrolling label, labels",sd="",web="",ext="") -> None:

        self.web= web
        self.nam = nam
        self.ext= ext
        ug =  5
        url=tl.img_read(nam)
        image1 = Image.open(url)
        new_width  = 138
        new_height = 200
        img = image1.resize((new_width, new_height), Image.Resampling.LANCZOS)

        l2 = ctk.CTkFrame(r,width= 400)
        divd = 1.06#1.015
        imgs = ctk.CTkImage(dark_image= img, size= (round(new_width/divd),round(new_height)/divd))
        self.label1 = ctk.CTkLabel(master= l2,image=imgs,text= "")
        self.label1.grid(padx= 5, pady = 5,ipadx= 2.5, ipady= 2.5)
 
        lab = ctk.CTkLabel(l2,text=(f"{nam}".replace("-"," ").title()), wraplength= 120, font= ("",10, "bold"), text_color= "gray", height= 20, width= 176)
        lab.place(x= -15,y= 5, anchor= tk.NW)
        lab.lift()

        self.label1.bind("<Enter>",self.show)
        self.label1.bind("<Leave>",self.hide)
        self.label2 = ctk.CTkButton(l2,text="⏬", font= ("", 24), width= 40)#,justify="center")
        self.label2.bind("<ButtonRelease-1>",self.adds)
        self.label2.bind("<Enter>",self.show)

    
    def show(self,event):
        self.label2.place(x= 20,y=100)#, height= 35)
        pass

    def hide(self,event):
        self.label2.place_forget()
        pass
    
    def adds(self,event):
        p = True
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt"

        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")
        
        for i in files:
            if i.split("|")[:2] == [self.nam,self.web]:
                p = False
        if p == True:
            tl.add(web=self.web,nam= self.nam)
            self.ext.clall()
