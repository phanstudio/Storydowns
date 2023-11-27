import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tools import Tools as tl
from down1 import Viewer2 as do
import customtkinter as ctk
import shutil
from pathlib import Path
import send2trash as snt
from tkinter import messagebox
import os


class Viewer2:
    add =[]
    clone = []
    y= 'pink'
    h = 0
    h3 = ['','','','']
    def __init__(self,u,inf,nif,hi,ipp,ico,ifo):
        self.ico = ico
        self.ifo = ifo
        self.inff = nif
        self.iop = ipp
        self.hi = hi
        self.ifff = inf
        self.u = u
        self.store()
        self.cll(self.inff,self.iop,self.hi)
        self.info = tl.read(inf)
        url = tl.img_read(self.info[0])
        image1 = Image.open(url)#"C:/Users/ajuga/OneDrive/Desktop/test/nec3.jpg")

        new_width  = 100
        new_height = 150
        img = image1.resize((new_width, new_height), Image.ANTIALIAS)

        self.r2 = ctk.CTkFrame(self.u,width= 70, height= 100, fg_color= "SystemButtonFace")
        divd = 0.921
        imgs = ctk.CTkImage(dark_image= img, size= (round(new_width/divd),round(new_height)/divd))
        self.label1 = ctk.CTkLabel(master= self.r2,image=imgs,text= "")#, highlightbackground= "pink")
        self.label1.pack(side= "left", padx= 2.5, pady = 2.5,ipadx= 2.5, ipady= 2.5)

        self.lab = ctk.CTkLabel(self.r2,text=(f"{self.info[2]}"), height= 20, font= ("", 12, "bold"), text_color= "white", )#"gray34")#, text_color= "blue")
        text_len = len(self.lab.cget("text"))
        self.lab.configure(width= 9*text_len, height= 18)
        self.lab.place(anchor=tk.NW,x= 5,y= 5)# adjutable length
        self.lab.lift()


        lab1 = ctk.CTkLabel(self.r2,text=(f"{self.info[0]}".replace("-"," ").title())
        , wraplength= 100, font= ("",10, "bold"), 
        height= 20, width= 136, text_color= "gray") #136, 100
        lab1.place(x= -10,y= 170, anchor= tk.SW)
        lab1.lift()

        self.label1.bind("<Button-1>",self.click)
        
        self.label1.bind("<Enter>",self.show)
        self.label1.bind("<Leave>",self.hide)
        self.label2 = ctk.CTkButton(self.r2,text="🗑️", font= ("", 11), width= 18, height=24, bg_color= "transparent")#,justify="center")
        self.color1 = self.label2.cget("fg_color")[1]
        self.label2.configure(fg_color = "red", bg_color= "red")
        self.lab.configure(fg_color= self.color1, bg_color= self.color1)
        self.label2.bind("<ButtonRelease-1>",self.removes)
        self.label2.bind("<Enter>",self.show)
        self.label2.bind("<Enter>",lambda x: self.label2.configure(bg_color= "#8b0000",fg_color= "#8b0000"), add= "+")
        self.label2.bind("<Leave>",lambda x: self.label2.configure(bg_color= "red",fg_color= "red"))
        #self.label1.bind("<Button-1>",lambda x: self.label2.configure(bg_color= "red",fg_color= "red"), add="+")
        self.label1.bind("<Enter>",lambda x: self.label2.configure(bg_color= "red",fg_color= "red"), add="+")
        self.label1.bind("<Enter>",lambda x: self.lab.configure(bg_color= self.color1), add="+")
        #self.label1.bind("<Button-1>",lambda x: self.lab.configure(bg_color= self.color1), add="+")

    
    def store(self):
        self.clone.append(self)

    def click(self,event):
        tl.inform(self.info)
        self.ifo.nums = tl.read(self.ifff)[:2]
        linf = tl.collect(self.ifo.nums[1],self.ifo.nums[0])
        linn = tl.digit_checker(linf[2].split(","))[-1]
        do.updatelab(linn)
        self.ifo.update(linf,int(self.info[2])) # books
        self.ico.update(self.info[0])
        self.clicked(self.r2,self.lab, self.color1)
        self.clad(self.r2)
        self.r2.configure(fg_color = self.color1)
        #self.lab.configure(bg_color= self.color1, fg_color= self.color1)
    
    @classmethod
    def clicked(cls,l,l1,l2):
        for i in cls.add:
            if i.configure("fg_color")!= "SystemButtonFace":
                i.configure(fg_color = "SystemButtonFace")
                break
        cls.add = []
        #
    
    @classmethod
    def clad(cls,l):
        #cls.add.append(l)
        
        cls.add = [l]
    
    @classmethod
    def clall(cls):
        cls.h3[0](cls.h3[1],cls.h3[2])
        #cls.h3[0](cls.iop,cls.hi)
        pass

    @classmethod
    def cll(cls,a,b,c):
        if cls.h == 0:
            cls.h=1
            cls.h3 = [a,b,c]
    
    def show(self,event):
        self.label2.place(x= 70,y=5)#, width= 34, height= 34)
        pass

    def hide(self,event):
        self.label2.place_forget()
        pass
    
    def rem(self):
        for i in self.clone:
            self.add = []
            if i.info[0] != self.info[0]:
                i.click("")
        pass

    def removes(self,event):
        self.hide("")
        self.clicked("","","")
        name, web = self.info[:2]
        path = Path("C:/Users/ajuga/OneDrive/Desktop/test") 
        libs = Path("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt")
        webs = Path(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/websites/{web}.txt")

        ext = True
        ett = False
        if ext == True:
            if messagebox.askokcancel("Delete".title(), f"Do you want to delete [{name}-({web})]?"):
                ett = True
        else:
            ett = True
        if ett == True:

            # create pop up are you sure
            # and func for instant delete

            #shutil.rmtree(path/ name)
            if os.path.exists(path/name):
                snt.send2trash(path/ name)

            with open(libs, "r")as f:
                data = f.read()
            with open(webs, "r")as f:
                data1 = f.read()

            data1 = [i.split("|") for i in data1.split("\n")]
            data = [i.split("|") for i in data.split("\n")]
            for j, i in enumerate(data1):
                if i[0] == name:
                    data1.pop(j)
                    break
            for j, i in enumerate(data):
                if i[0] == name and i[1] == web:
                    data.pop(j)
                    break

            #print(i[:2], "Removed")
            data1 = "\n".join(["|".join(i) for i in data1])
            data = "\n".join(["|".join(i) for i in data])
            

            with open(libs, "w")as f: # removing from the library
                f.write(data)
            with open(webs, "w")as f: # removing from the websites
                f.write(data1)
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/lib1.txt","w") as f:
                f.write("")
            
            for j in self.u.winfo_children():
                j.grid_forget()
                j.destroy()
            

            self.clone = []
            self.inff(self.u, self.hi)
            self.rem()
        pass



