from tkinter import Tk, ttk
import tkinter as tk
import os
from tools import Tools as tl
import customtkinter as ctk


class Viewer:
    nums = tl.inform(op="r")[:-1]#tl.read(0)[:-1]#['i-hate-systems','novelhard']
    @classmethod
    def views(cls,u,wth,inf):
        info = inf
        widt = 250
        hegt = 400
        cls.wth = wth
        cls.widt = widt

        pad = 15
        def unit(widths= 600, div= 64, per = "57/7", pad_div= 1.2):
            widt_unit = widths/div
            li = []
            for i in per.split("/"):
                li.append((widt_unit*int(i)) - (pad/pad_div))
            return li

        hegt1 = unit(hegt, 32, "4/28",0.8)
        widt1 = unit(widt, 32, "26/6",0.8)
        sep1 = round(widt/9.090909090909092)
        
        cls.txt = cls.up(widt,info,6)#wth)
        # main frame
        #r1 = ctk.CTkFrame(u,)

        r3 = ctk.CTkFrame(u,width= widt, height= hegt) # add code to the padding
        #r3.pack(expand= True, fill= "both",pady= 15, padx= 15)

        # Total chapter frame
        r5 = ctk.CTkFrame(r3,width= widt - pad, height= hegt1[0], fg_color= "transparent")
        r5.pack(side= "top",fill= "both", padx= 15, pady = 5)
        infx = tl.inform(op="r")
        cls.lab3 = ctk.CTkLabel(r5,text= (infx[2]+" Chapters"), font= ("TkDefaultFont",18),anchor="w", width= widt+pad)
        cls.lab3.pack(fill= "both", expand= True)

        # r6 = ctk.CTkFrame(r3,width= widt1[0], height= hegt - pad)
        # r6.pack(fill= "both",ipadx= 5, side= "left")

        # rigth frame
        cls.t12 = cls.drr(r3,sep1-wth,cls.txt,info)
        cls.t12.pack(fill= "both", padx= 5, pady= 5)

        return r3

    @classmethod
    def drr(cls,r1, wi,txt,info):
        # create the text widget
        text = ctk.CTkTextbox(r1, height= 300, width= 270)#, fg_color= None)#, activate_scrollbars= False)#, width= wi+12)
        # ctk.ct

        #create a scrollbar widget and set its command to the text widget
        # scrollbar = ctk.CTkScrollbar(r1, command=text.yview,orientation="vertical")
        # scrollbar.pack(side= "left", fill= "y")

        #  communicate back to the scrollbar
        #text['yscrollcommand'] = scrollbar.set
        # text.configure(yscrollcommand= scrollbar.set)

        # add sample text to the text widget to show the screen
        #self.tree.insert("", "end", text= i[2], values=(*i[1:], item_path))
        # try tree
        text.configure(state='normal')
        infx = tl.inform(op="r") #fix this
        for i in range(1,int(infx[2])+1):
            position = f'{i}.0'
            text.insert(position,txt.split("\n")[i-1]+"\n")
        text.delete(int(infx[2])+1.0,"end")
        text.configure(state='disabled')
        return text

    @classmethod
    def up(cls,widt,info,wth= 5, siz= "000"):
        sep = round(widt/6.976744186046512)
        err = round(((widt-300)/14.285714285714286))
        d = " "*wth
        d5 = "00:00"
        lu = []
        lx = []
        di7 = "✅❎⚠️"
        y9 = di7[0]
        t = 0
        k = " "*33#75
        l = int(tl.inform(op="r")[2])
        if siz != "000": l = siz
        for i in range(1,l+1):
            j = " "*6
            if i > 9:
                j = " "*4
            if i > 99:
                j = " "*2

            if i == int(tl.digit_checker(info[2].split(","))[t]):
                d5 = tl.time_converter(info[3].split(",")[t])
                y9 = di7[0]
                if i != int(tl.digit_checker(info[2].split(","))[-1]):
                    t += 1
            else:
                d5 = "00:00"
                y9 = di7[1]

            lu.append(f"Chapter {i}{k}{j}{d}{d5}{y9}\n")
            
        txt = "".join(lu)
        return txt

    @classmethod
    def update(cls,inf,si,num= 0):
        info = inf
        cls.txt = cls.up(cls.widt,info,6,si)
        cls.lab3.configure(text= f"{si} Chapters")
        cls.t12.configure(state='normal')

        if num == 0:
            cls.t12.delete("1.0","end")
            for i in range(1,si+1):
                position = f'{i}.0'
                cls.t12.insert(position,cls.txt.split("\n")[i-1]+"\n")
            cls.t12.delete(si+1.0,"end")
        else:
            cls.t12.delete(str(num)+".0",str(num)+".end")
            cls.t12.insert(str(num)+".0", cls.txt.split("\n")[num-1])
        cls.t12.configure(state='disabled')

if False:
    # @classmethod
    # def upp(cls,nam):
    #     inf = tl.inform(op="r")
    #     t = " "*(67-len(inf[0]))
    #     cls.lab1['text'] = f"{inf[0]}{t}".title().replace("-"," ")
    #     cls.lab3['text'] = f"ʘ•Ongoing•{inf[1]}.com{t}".title()

    #     image1 = Image.open(tl.img_read(nam))
    #     new_width  = 100
    #     new_height = 150
    #     img = image1.resize((new_width, new_height),  Image.Resampling.LANCZOS)
    #     test = ImageTk.PhotoImage(img)
    #     cls.label1.configure(image=test)
    #     cls.label1.image = test
    pass


