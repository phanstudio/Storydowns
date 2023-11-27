import tkinter as tk
from tkinter import ttk
from tools import Tools as tl
from tester import Downs
import random as rd
from tkinter.messagebox import showerror
import customtkinter as ctk
import pyttsx3 as pytts

def unit(widths= 600, div= 64, per = "57/7", pad_div= 1.2):
    widt_unit = widths/div
    li = []
    for i in per.split("/"):
        li.append((widt_unit*int(i)) - (15/pad_div))
    return li

def processD(dat="", old="", cust= False):
    if not dat.isnumeric() and "-" not in dat: return "ERROR!: input should be a number"
    if int(dat) < 0: return "ERROR!: input shouldn't be a negative number"
    if old == "": return dat
    if cust == True: 
        if int(dat) > int(old): return "ERROR!: The 1st number greater than other number"
        return "{}-{}".format(dat,old)
    dat = int(old)+int(dat)
    if dat-1 == int(old): return str(dat)
    return "{}-{}".format(old,dat)



class Viewer2:
    val = 0.0
    @classmethod
    def views(cls,u,inf,vrr):
        cls.vrr = vrr
        cls.root = u
        cls.clicked = False
        info = inf
        widt = 400
        hegt = 400

        hegt1 = unit(hegt, 32, "3/3/21/5",1.4)
        hegt2 = unit(hegt1[2]+100, 32, "5/5/5/5/12",0.8) #75
        vcmd = (u.register(cls.callback))

        p7 = " "*22
        cls.update()

        if True:# MAIN FRAMES
            r3 = ctk.CTkFrame(u,width= widt, height= hegt - 15)

        if True:# CURRENT FRAME
            r5 = ctk.CTkFrame(r3,height= hegt1[0], fg_color= "transparent")
            r5.pack(fill= "x",padx=5, pady=5)
            ctk.CTkLabel(r5,text= "📖",anchor= tk.S,width= 20,font=("TkDefaultFont",18)).pack(side="left")
            cls.lab4 = ctk.CTkLabel(r5,text= f"Current Number of Downloaded Chapter({cls.p})".title(),anchor= tk.S)
            cls.lab4.pack(side="left",fill= "x", padx= 1)

        if True:# SMALLEST FRAME
            r6 = ctk.CTkFrame(r3,height= hegt1[1], fg_color= "transparent")
            r6.pack(fill= "x",padx= 5)
            ctk.CTkLabel(r6,text= "📗",anchor= tk.N,width= 20,font=("TkDefaultFont",18)).pack(side="left")
            cls.lab5= ctk.CTkLabel(r6,text= f"Smallest Downloaded Chapter({cls.p2})".title(),anchor= tk.CENTER)
            cls.lab5.pack(side="left",fill= "x")


        if True:# Container
            r7 = ctk.CTkFrame(r3,height= hegt1[2],fg_color= "transparent")#,fg_color= color1)#color)
            r7.pack(fill= "both" ,padx=5,pady=5)
            r8 = ctk.CTkFrame(r7,height= hegt1[2]-5,width= 500, fg_color= "transparent")
            r8.pack(fill= "both",side="left")#,pady=5)

        if True:# Download Icon
            #r6 = ctk.CTkFrame(r8,height= hegt1[2],width= 500)
            #r6.pack(fill= "y",side="top")
            ctk.CTkLabel(r8,text= "⏬",anchor= tk.CENTER,width= 10,font=("",14), justify= "left").pack(fill= "y",side= "top")
            #ttk.Label(r8,background= "white",anchor= tk.N).pack(side= "top",fill= "y")
            pass


        if True: # Container and Next Chapter
            ry = " "*62
            r101 = ctk.CTkFrame(r7,height= hegt1[2]- 24,width= 400, corner_radius= 5)#, fg_color= "transparent")#, fg_color= color)
            r101.pack()#side="left",fill= "y",pady = 2.5,padx=2.5)
            r10 = ctk.CTkFrame(r101,height= hegt1[2]- 24,width= 400, corner_radius= 5)#, fg_color= "transparent")#, fg_color= color)
            r10.pack(side="left",fill= "y",pady = 2.5,padx=2.5)
            cls.lab = ctk.CTkLabel(r10,text= f"Next Chapter",anchor="w", width= 400)
            cls.lab.bind("<Button>",cls.click2)
            cls.lab.bind("<Enter>", cls.high, add= "+")
            cls.lab.pack(fill= "x",side= "top", padx= 5)

        if True:# Next Chapters
            r12 = ctk.CTkFrame(r10,height= hegt2[1],width= 400, fg_color= "transparent")
            r12.pack(fill= "x", padx= 5,pady= 2.5)
            ctk.CTkLabel(r12,text= f"Next ",justify= "left",anchor="w", width= 30).pack(fill= "x", side= "left")
            cls.e3 = ctk.CTkEntry(r12, width= 43, validate='all', validatecommand=(vcmd, '%P'))
            cls.e3.bind("<FocusIn>",cls.hide1)
            cls.e3.bind("<FocusIn>",cls.show1, add= "+")
            cls.e3.pack(fill= "x", side= "left")
            ctk.CTkLabel(r12,text= f" Chapters",justify= "left",anchor="w",width= 50).pack(fill= "x", side= "left")
            cls.but1=  ctk.CTkButton(r12,text= "⏬",width= 80,command=cls.click)
            
        if True:# Chapter (only)
            r13 = ctk.CTkFrame(r10,height= hegt2[2],width= 400,fg_color= "transparent")
            r13.pack(fill= "x", padx= 5, pady=2.5)
            ctk.CTkLabel(r13,text= f"Chapter ",anchor="w",width= 20).pack(fill= "x", side= "left")
            cls.e4 = ctk.CTkEntry(r13, width= 43, validate='all', validatecommand=(vcmd, '%P'))
            cls.e4.bind("<FocusIn>",cls.hide2)
            cls.e4.bind("<FocusIn>",cls.show2, add= "+")
            cls.e4.pack(fill= "x", side= "left")
            ctk.CTkLabel(r13,text= f" (ONLY)",anchor="w",width= 50).pack(fill= "x", side= "left")
            cls.but2 = ctk.CTkButton(r13,text= "⏬",width= 80,command=cls.click,)

        if True:# Multiple Chapters and Black space
            r15 = ctk.CTkFrame(r10,height= hegt2[3],width= 400,fg_color= "transparent")
            r15.pack(fill= "x", padx= 5,pady= 2.5)
            ctk.CTkLabel(r15,text= f"Multiple Chapters From ",anchor="w", width= 20).pack(fill= "x", side= "left")
            cls.e1 = ctk.CTkEntry(r15, width= 43, validate='all', validatecommand=(vcmd, '%P'))
            cls.e1.bind("<FocusIn>",cls.hide3)
            cls.e1.bind("<FocusIn>",cls.show3, add= "+")
            cls.e1.pack(fill= "x", side= "left")
            ctk.CTkLabel(r15,text= f" TO ",anchor="w",width=20).pack(fill= "x", side= "left")
            cls.e2 = ctk.CTkEntry(r15, width= 43, validate='all', validatecommand=(vcmd, '%P'))
            cls.e2.bind("<FocusIn>",cls.hide3)
            cls.e2.bind("<FocusIn>",cls.show3, add= "+")
            cls.e2.pack(fill= "x", side= "left")
            cls.but3 = ctk.CTkButton(r15,text= "⏬",width= 80,command=cls.click)

        if True:# Voice
            r17 = ctk.CTkFrame(r10,height= hegt2[2],width= 400,fg_color= "transparent")
            r17.pack(fill= "x", padx= 5,pady=2.5)
            ctk.CTkLabel(r17,text= f"Voice: ",anchor="w",width= 20).pack(fill= "x", side= "left")
            lo = [i.name for i in pytts.init().getProperty("voices")]
            cls.opt1 = ctk.CTkOptionMenu(r17,values= lo)
            cls.opt1.pack(side= "left", padx=5)
            for i in range(len(lo)):
                if tl.setters("r", "Voices") == lo[i]:
                    liio =  i
            cls.opt1.set(lo[liio])

        ctk.CTkFrame(r10,height= hegt2[4]+30, fg_color= "transparent").pack(fill= "x", padx= 5)

        if True:# PROGRESSBAR FRAME
            r14 = ctk.CTkFrame(u,height= hegt1[3])
            r14.pack(fill= "x",side="bottom",padx= 5,pady=5)
            cls.lab3 = ctk.CTkLabel(r14,text= f"Next Chapter({cls.p4})".title(), justify= tk.LEFT,anchor="w")
            cls.lab3.pack(fill= "x",padx=5,pady=5)
            ctk.CTkLabel(r14,text= "⏬",anchor= tk.CENTER,width= 10,font=("",14), justify= "left").pack(side="left",padx=5)
            cls.pb = ctk.CTkProgressBar(
                r14,
                orientation='horizontal',
                mode='determinate',
                width= 350,
                height=10,
                determinate_speed= 2,
                
            )
            cls.pb.pack(fill= "x",side= "left",padx=5)
            cls.pb.set(1)
        
        return r3

    @classmethod
    def hide1(cls,event):
        cls.e1.delete(0,tk.END)
        cls.e2.delete(0,tk.END)
        cls.e4.delete(0,tk.END)

    @classmethod
    def hide2(cls,event):
        cls.e1.delete(0,tk.END)
        cls.e2.delete(0,tk.END)
        cls.e3.delete(0,tk.END)

    @classmethod
    def hide3(cls,event):
        cls.e3.delete(0,tk.END)
        cls.e4.delete(0,tk.END)

    @classmethod
    def click2(cls,event):
        cls.update()
        if cls.clicked == True: return "break"
        cls.clicked = True
        prt = processD("1",cls.p4)
        cls.e1.delete(0,tk.END)
        cls.e3.delete(0,tk.END)
        cls.e2.delete(0,tk.END)
        cls.e4.delete(0,tk.END)
        cls.but1.pack_forget()
        cls.but2.pack_forget()
        cls.but3.pack_forget()
        cls.lab.focus()

        cls.pb.set(0)
        tl.setters("w", "Voices", cls.opt1.get())
        download_thread = Downs(prt,val=cls.vrr, prog=cls.pb,lab= cls.updatelab, err= cls.err,gen= cls.opt1.get())
        download_thread.start()
        cls.pb.set(cls.val)
        cls.monitor(download_thread)

    @classmethod
    def click(cls):
        cls.update()
        if cls.clicked == True: return "break"
        cls.clicked = True
        if cls.e1.get() and cls.e2.get():
            prt = processD(cls.e1.get(),cls.e2.get(),True)
        if cls.e3.get():
            prt = processD(cls.e3.get(),cls.p4)
        if cls.e4.get():
            prt = processD(cls.e4.get())
        cls.e1.delete(0,tk.END)
        cls.e3.delete(0,tk.END)
        cls.e2.delete(0,tk.END)
        cls.e4.delete(0,tk.END)
        
        cls.lab.focus()
        cls.but1.pack_forget()
        cls.but2.pack_forget()
        cls.but3.pack_forget()

        cls.pb.set(0)
        tl.setters("w", "Voices", cls.opt1.get())
        download_thread = Downs(prt,val=cls.vrr, prog=cls.pb,lab= cls.updatelab, err= cls.err,gen= cls.opt1.get())
        download_thread.start()
        cls.pb.set(cls.val)
        cls.monitor(download_thread)

    @classmethod
    def monitor(cls, thread):
        if thread.is_alive():
            # check the thread every 100ms
            if cls.pb.get() < 1:
                cls.val += 0.002 #rd.choice((0.01,0.0105,0.011,0.0115,0.012,0.0125))
                cls.pb.set(cls.val)
            cls.root.after(100, lambda: cls.monitor(thread))
        else:
            cls.clicked = False
            cls.update()
            cls.val = 0
            pass

    @classmethod
    def show1(cls,event):
        cls.but1.pack(fill= "x", side= "right")
        cls.but2.pack_forget()
        cls.but3.pack_forget()

    @classmethod
    def show2(cls,event):
        cls.but2.pack(fill= "x", side= "right")
        cls.but1.pack_forget()
        cls.but3.pack_forget()

    @classmethod
    def show3(cls,event):
        cls.but3.pack(fill= "x", side= "right")
        cls.but2.pack_forget()
        cls.but1.pack_forget()

    @classmethod
    def high(cls,event):
        #lab.configure
        pass

    @classmethod
    def callback(cls, P):
        if (str.isdigit(P) and int(P) < 9999) or  P == "":
            return True
        else:
            return False

    @classmethod
    def update(cls):
        cls.p1 = tl.digit_checker(tl.collect(cls.vrr.nums[1],cls.vrr.nums[0])[2].split(","))#cls.vrr.nums[1],cls.vrr.nums[0])[2].split(","))
        cls.p4 = cls.p1[-1]
        cls.p2 = cls.p1[0]
        cls.p = len(list(map(int,cls.p1)))
        if cls.p1 == ["0","0","0","0"]: cls.p = 0

    @classmethod
    def updatelab(cls,num):
        cls.val = 0 
        cls.p1 = tl.digit_checker(tl.collect(cls.vrr.nums[1],cls.vrr.nums[0])[2].split(","))
        cls.p2 = cls.p1[0]
        cls.p = len(list(map(int,cls.p1)))
        if cls.p1 == ['0', '0', '0', '0']: cls.p = 0
        #cls.p = len(list(map(int,cls.p1)))
        p7 = " "*22
        cls.lab4.configure(text = f"Current Number of Downloaded Chapter({cls.p})")
        cls.lab3.configure(text = f"Next Chapter({num})".title())
        cls.lab5.configure(text = f"Smallest Downloaded Chapter({cls.p2})".title())

    @classmethod
    def err(cls):
        cls.pb.set(1)
        showerror("Bad Network","Unfortuately you have bad network and we advise you to try again later")




