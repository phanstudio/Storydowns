import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tools import Tools as tl
import customtkinter as ctk


class Webp():
    webs = []
    typp = 0
    ope = False
    def __init__(self,r,nam= "NovelHard",url="C:/Users/ajuga/OneDrive/Desktop/test/clas_4.jpg", rls= "", ll= "", ext="") -> None:
        img = Image.open(url)
        new_width  = 138
        new_height = 200
        self.rls = rls
        self.ll = ll
        self.nam =  nam
        self.ext = ext

        # url = 'https://path.to/image.png' # online viewing img
        # response = requests.get(url)
        # load = Image.open(BytesIO(response.content))

        l2 = ctk.CTkFrame(r, fg_color= "SystemButtonFace")
        divd = 1.5#1.06
        imgs = ctk.CTkImage(dark_image= img, size= (round(new_width/divd),round(new_height)/divd))
        self.label1 = ctk.CTkLabel(master= l2,image=imgs,text= "")
        self.label1.pack(padx= 5, pady = 5,ipadx= 2.5, ipady= 2.5)
 
        lab = ctk.CTkLabel(self.label1,text=(f"{nam}".replace("-"," ").title()), wraplength= 90,
         font= ("",10, "bold"), text_color= "gray", height= 20,width= 120)#, fg_color= "black")
        lab.place(x= -10,y= 0, anchor= tk.NW)
        lab.lift()

        self.label1.bind("<Enter>",self.show)
        self.label1.bind("<Leave>",self.hide)
        self.label2 =  ctk.CTkButton(l2,text="⏬", font= ("", 24), width= 40)#,justify="center")
        self.label2.bind("<ButtonRelease-1>",self.adds)
        self.label2.bind("<Enter>",self.show)

    
    def show(self,event):
        self.label2.place(x= 20,y=100)#, height= 35)
        pass

    def hide(self,event):
        self.label2.place_forget()
        pass
    
    def adds(self,event):
        rlz = self.ll.lower()
        for i in self.rls.split('/'):
            
            if self.nam.lower().split()[0].replace(":","").replace("'","") in i:
                print(i)
                rls = i
                break
        p = True
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt"

        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")
        
        for i in files:
            if i.split("|")[:2] == [rls,rlz]:
                p = False
        if p == True:
            tl.add(web=rlz,nam= rls)
            self.ext.clall()

class Frammer():
    def __init__(self,r,nam= "NovelHard", li=[], ly=[],ext= "", theme_c= 0, cont= '', term="") -> None:
        if term == "":
            ctk.CTkLabel(r, text= nam.title(), font= ("",15, "bold")).pack(pady=2.5)
            scrollable_frame = ctk.CTkScrollableFrame(r, width= 900,height= 170, orientation= "horizontal", )
            #label_text= "no searches".title(), label_fg_color= None)

            self.scrollable_frame = scrollable_frame
            self.ext = ext
            self.nam = nam
            self.ly = ly
            self.li = li
            self.term = term 

        scrollable_frame.pack(padx= 5, pady= 5)

    def doo(self, li, ly, ext):
        for j,i in enumerate(li):
            if type(i) != list:
                Webp(self.scrollable_frame, str(i),rls= ly[j], ll= self.nam, ext= ext)
            else:
                Webp(self.scrollable_frame, str(i[0]), i[1],rls= ly[j], ll= self.nam, ext= ext)

        for i in self.scrollable_frame.winfo_children():
            i.pack(side= "left", padx= 2.5, pady= 5)
