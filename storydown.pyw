from tkinter import Tk, ttk
import tkinter as tk
from Books import Viewer
from info_title import Viewers
from down1 import Viewer2
from tools import Tools as tl
from libra import Viewer2 as lib
import random as rd
from web import Webp as Web
from webc3 import Webp2 as Web1
from tkinter import messagebox
from novs import Novel as nov
from PIL import Image, ImageTk
import threading


from searcher import Frammer as searc
import time
import requests
import bs4
import threading
import datetime as dt

import win32gui, win32con, urllib.request
import customtkinter as ctk

Aadmin = True

if Aadmin == False:
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

theme_s = int(tl.setters("r", "Theme"))
theme_c = 0
if theme_s == 0:
    ctk.set_appearance_mode("dark")
    theme_c = 1
else:
    ctk.set_appearance_mode("light")
    theme_c = 0
ctk.set_default_color_theme("dark-blue")#"green")#"green")#"dark-blue")
r = ctk.CTk()
info = tl.collect(web =tl.inform(op="r")[1], nam= tl.inform(op="r")[0])
widt = 1050
hegt = 600
pad = 15
ext = True#False # set

r.title("story downloader")
r.geometry(f"{widt}x{hegt}")
r.resizable(width=False, height= False)

ddd = r"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/script/Azure-ttk-theme-main/azure.tcl"
r.tk.call("source", ddd)
r.tk.call("set_theme", "dark")

tabview = ctk.CTkTabview(r)
tabview.pack(padx=10, pady=10)
tab1 = tabview.add("Home")
tab6 = tabview.add("Update")
tab2 = tabview.add("Browse")
tab3 = tabview.add("Search")
tab4 = tabview.add("Settings")
tab5 = tabview.add("Admin(Add)")

if Aadmin == False: # Admin(Add) adjuster
    tabview.delete("Admin(Add)")
tabview.set("Home")  # set currently visible tab
r1 =  ctk.CTkFrame(master=tab1)
w1 =  ctk.CTkFrame(tab2)
w2 =  ctk.CTkFrame(tab3)
w3 =  ctk.CTkFrame(tab4)
q1 =  ctk.CTkFrame(tab5)
tr1 = ctk.CTkFrame(tab6)

if True: # func
    # with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","w") as f:
    #     f.write("")
    
    def net_check(host):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    def unit(widths= 600, div= 64, per = "57/7",pad_div = 1.2):
        widt_unit = widths/div
        li = []
        for i in per.split("/"):
            li.append((widt_unit*int(i)) - (pad/pad_div))
        return li

    def themx(them,c,l,s):
        for i in range(len(c)):
            c[i].configure(background= l[i][them], highlightbackground= l[i][them])
            s[i].configure(fg_color=l[i][them], bg_color=l[i][them])
        
        with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
            file = f.read()
            file = file.split("\n")

        for i in scrollable_frame34.winfo_children():
            lif = [f"!ctkframe{i+1}" for i in range(len(file))]
            lif[0] = lif[0][:-1]
            if i.winfo_name() in lif:
                for j in i.winfo_children():
                    lif1 = [f"!ctkcanvas{i+1}" for i in range(len(file))]
                    lif1[0] = lif[0][:-1]
                    if j.winfo_name() in lif1:
                        for lw in range(len(c)):
                            j.configure(background= l[lw][them], highlightbackground= l[lw][them])
                            for k in j.winfo_children():
                                k.configure(fg_color=l[lw][them], bg_color=l[lw][them])                    
        pass

    def loadbar(l):
        l += 1
        return l
    
    def lo2d(files1, files3):
        j = []
        llp= []
        for i in files1:
            f = i
            fv = i[:2] + ["0"] + [i[2]]
            for k in files3:
                if i[0].replace(" ","-").lower() == k[0]:
                    if k[1] > i[2]:
                        fv = [*i[:2], str(int(k[1])-int(i[2])), i[2]]
                        f = [*i[:2],k[1]]
                    break
            if int(fv[2]) != 0:
                llp.append(fv)
            j.append("|".join(f))
        
        j = "\n".join(j)

        loo = []
        for iio in llp:
            loo.append(iio[0]+ " {%s}"%(iio[1]) + "\p" + "|".join(["Chapter " + str(iion) 
            for iion in range(int(iio[3]) + 1, int(iio[3]) + int(iio[2]) + 1)][-20:]))
        gt = str(dt.date.today())
        loo = [gt] + loo
        if len(loo) > 1:
            loo = "\n".join(loo) #+ "\n"
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/logg.txt","a") as f:
                f.write(loo)
        
        #print("\n".join(["|".join(jjk) for jjk in files1]), "\n".join(["|".join(jjn) for jjn in files3]), sep="\n"*3)
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt","w") as f:
            f.write(j)
            pass

        jji = [i.split("|")[2] for i in j.split("\n")]
        for fc,fg in enumerate(scrollable_frame3.winfo_children()):
                for lf,fl in enumerate(fg.winfo_children()):
                    #print((fc*2)+lf, len(jji))
                    #print(fl.winfo_name())
                    if fl.winfo_name() == "!ctklabel2":
                        if (fc*2)+lf < len(jji):
                            #print(fl.winfo_children()[1])
                            #break
                            fl.winfo_children()[1].configure(text = f"{jji[(fc*2)+lf]}") #fix num

    def yes_tod(gt):
        gy = dt.datetime.strptime(gt,r"%Y-%m-%d")
        gty = dt.date.today()
        if gty.day == gy.day and gty.month == gy.month and gty.year == gy.year:
            return "Today"
        elif gty.day-1 == gy.day and gty.month == gy.month and gty.year == gy.year:
            return "Yesterday"
        else:
            return gy

    def tLoad():
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt","r") as f:
            files1 = [i.split("|") for i in f.read().split("\n")]
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","r") as f:
            files3 = [i.split("|") for i in f.read().split("\n")[:-1]]
        lo2d(files1, files3)
        if len(files1) == len(files3):
            #lo2d(files1, files3)
            print("done!")
        else:
            r.after(3750, tLoad)
            pass
        
    def total_get(
        p = "peerless-martial-god-073022",
        web = "www.readlightnovel.me",
        mess = ".error-message"
    ):
        mayo = 500
        message = p+f" done({mayo}) 0"
        
        if mess != "":
            s = requests.Session()
            lx = 0
            start_time = time.time()
            if True:
                for i in range(8):
                    j = 50*(2** i)
                    url = f"https://{web}/{p}/chapter-{j}/"
                    res = s.get(url)
                    soup = bs4.BeautifulSoup(res.text, "lxml")
                    h = soup.select(f"{mess}")
                    if h != []: break
                    lx = loadbar(lx)

                j1 = j/2
                j2 = j
                for _ in range(30):
                    r = round((j2 + j1)/2)
                    url = f"https://{web}/{p}/chapter-{r}/"
                    res = s.get(url)
                    soup = bs4.BeautifulSoup(res.text, "html.parser")
                    h = soup.select(f"{mess}")
                    lx = loadbar(lx)
                    #print(r)
                    if h != []:
                        j2 = r
                        lx = loadbar(lx)
                        # print(r)
                    else:
                        url = f"https://{web}/{p}/chapter-{r+1}/"
                        res = s.get(url)
                        soup = bs4.BeautifulSoup(res.text, "html.parser")
                        h1 = soup.select(f"{mess}")
                        # print(r)
                        if h1 != []: 
                            message = "-"*lx + f"{p} done({r}) "
                            mayo = r
                            # os.system("cls||clear"); print("-"*lx,f"done({r}) ", end= '')
                            break
                        else:
                            j1 = r
                            lx = loadbar(lx)
                            # print(r)
            final_time = time.time()

            tim = final_time - start_time
            message = message + str(round(tim))
        #print(message+"sec", "-----", mayo)
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","r") as f:
            pgg = f.read()
        if len(pgg) != 0:
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","a") as f:
                #print(p,mayo)
                f.write(f"{p}|{mayo}\n")
                #files = files.split("\n")
        else:
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","w") as f:
                f.write(f"{p}|{mayo}\n")
            

        pass

    def on_closing():
        tl.setters("w", "Voices", Viewer2.opt1.get())
        ext = int(tl.setters("r", "Confirm Exit"))
        ett = False
        if ext == True:
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                ett = True
        else:
            ett = True
        if ett == True:
            if Aadmin == False:
                active_window = win32gui.GetForegroundWindow()
                win32gui.PostMessage(active_window, win32con.WM_CLOSE, 0, 0)
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/web2.txt","w") as f:
                f.write("")
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/lib1.txt","w") as f:
                f.write("")
                r.destroy() # error
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/sea.txt","w") as f:
                f.write("")
            # with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","w") as f:
                #f.write("")
                # pass
            pass

    def reload():
        print(2)
        # improve 
        # Add code to destroy all threads
        r.after_cancel(savv(1,f="r"))
        savv(0,val= "False")
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_fm.txt","w") as f:
            f.write(str(0))
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot.txt","w") as f:
            f.write("")
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_bat.txt","w") as f:
            f.write("")
        updt()

if True: # Home
    widt1 = unit(widt, 64, "57/7")
    widt1_1, widt1_2 = unit(widt1[0], 8, "2/6")
    widt2 = unit(widt1_2, 24, "7/17")
    widt3 = unit(widt1_2, 4, "1/3")

    # content frame
    r4 = ctk.CTkFrame(master= r1,width= widt1[0], height= hegt - pad, fg_color= "transparent")
    r4.pack(expand= True, fill= "both", pady= 5, padx= 5,ipadx= 5,side="left")

    # libary frame
    if True:
        scrollable_frame3 = ctk.CTkScrollableFrame(r4, width= 250,)

        def upsss(scrollable_frame3,widt1_1):
            pad = 15
            nhn = 2
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt","r") as f:
                file5 = f.read()
            file5 = file5.split("\n")
            numsb = len(file5)
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/lib1.txt","r") as f:
                loads = f.read()
                
            if loads == "":
                for  hjh in range(numsb):
                    lib(scrollable_frame3,hjh,upsss,widt1_1,scrollable_frame3,Viewers,Viewer)
                
                lop = -1
                for g,j in enumerate(scrollable_frame3.winfo_children()):
                    popl = round((g/2)-0.1)
                    if lop != popl:
                        lop = popl
                        for uiu in range(2):
                            if (2*popl)+uiu+1 <= numsb:
                                scrollable_frame3.winfo_children()[(2*popl)+uiu].grid(pady= 5, padx= 5, column=uiu, row=popl)  
            else:
                if numsb != int(loads) and numsb > int(loads):
                    lib(scrollable_frame3,numsb-1,upsss,widt1_1,scrollable_frame3,Viewers,Viewer)
                    scrollable_frame3.winfo_children()[-1].grid(pady= 5, padx= 5, column=(int(loads))%2, row=(int(loads))//2)
                    pass
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/lib1.txt","w") as f:
                f.write(f"{numsb}")
        
        upsss(scrollable_frame3,widt1_1)
        scrollable_frame3.pack(fill= "both",expand= True, padx= 7.5, pady= 7.5, side= "left")

    # main frame
    r6 = ctk.CTkFrame(master= r4,width= widt1_2, height= hegt - pad)
    r6.pack(fill= "both", pady= 5, padx= 5,side="right")

    li = []
    for i in range(2):
        li.append(ctk.CTkFrame(master=r6,width= sum(widt2)-pad, height= widt2[i]))

    Viewers.views(r6,info).pack(fill= "both", padx= 5.5, pady= 5, ipady= 5)
    o = Viewer2.views(li[1],info,Viewer)
    rx = Viewer.views(r6,4,info)

    rx.pack(fill= "both",side= "left", padx= 5.5,pady= 5)
    o.pack(fill= "both", side= "right",padx= 5,pady= 5)

    li[1].pack(pady = 5,side= "top",padx= 5)

    r1.pack(expand= True, fill= "both",pady = 10, padx= 10)

if True: # Admin(Add)
    ridt1 = unit(widt, 32, "21/13",pad_div= 0.31)
    # q3 = ctk.CTkFrame(q1)#,style= 'new.TFrame', padding= 5)
    # q3.pack(expand= True, fill= "both", padx= 5, pady= 5)

    if True: #add scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(q1, width= 670, height= 600)
        
        def update():
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
                file = f.read()
                file = file.split("\n")

            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/web2.txt","r") as f:
                lpp = f.read()
                if lpp != "": lpp = lpp.split("\n")
                else: lpp = []
            
            for i in range(len(file)):
                lo = file[i].split("|")
                if lo[0] not in lpp:
                    txt = f"Rating: {rd.randint(0,5)}/5"
                    n = lo[0]
                    Web(scrollable_frame,n,txt=txt+" "*(50-len(txt)), ev1= "",ev2="",ev3= "")
                    lpp.append(lo[0])
                    #scrollable_frame.bind("<Expose>",nnn)
            
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/web2.txt","w") as f:
                file = f.write("\n".join(lpp))

            gd = 2
            scf = scrollable_frame.winfo_children()
            for huh, i in enumerate(scf):
                i.grid_forget()
                i.grid(padx= 5, pady= 5, column= huh%gd, row= huh//gd)
            #scrollable_frame.after(1000,update)

        update() #change this to only when adding
        scrollable_frame.pack(side= "left", fill= "both", padx= 5, pady= 5)

    just_c = 70
    q5 = ctk.CTkFrame(q1,width= ridt1[1], height= hegt - pad)
    q5.pack(fill= "both",ipadx= 5, side= "right", padx= 5, pady= 5)
    ctk.CTkLabel(q5, text=f"Add Websites-[NEW]".center(just_c+10).upper(), font= ("", 12, "underline","bold")).pack(side= "top",pady= 5,padx=5)
    q55 = ctk.CTkFrame(q5, fg_color='transparent')
    q55.pack(fill= "both",ipadx= 5, side= "top", padx= 5, pady= 5)
    ol = ["W-Link","W-Error","W-Extn","CName","Search","W-Instl"] #"W-Instl" #W-ids

    class parameter():
        def __init__(self, nam="Name") -> None:
            q6 = ctk.CTkFrame(q55,width= ridt1[1]-10, fg_color= "transparent")
            ctk.CTkLabel(q6, text= f"{nam}:", width= 55, anchor= "w").pack(side= "left",padx= 5)
            ctk.CTkEntry(q6, width= 200).pack(side= "right")#180
        
        def gett(self):
            pass
    for i in ol:
        p = parameter(i)
    for j in q55.winfo_children():
        j.pack(fill= "x",ipadx= 5, side= "top", pady = 5, padx= 5)
    if True: #validator
        import validators
        def validate(
            web = "novelhard.com",
            error = "#btn-read-first",
            ext = "light-novel",
            chap_nam = "chapter-",
            *args,
            ids= "h3>"):

            nam = web.split(".")[0]
            url = f"https://{web}"
            valid=validators.url(url)
            if valid==True:
                pass
            else:
                print("Invalid url")
            ext = "/"+ext+"/"
            tl.installer(url,ids)
            
            #Store
            if len(args) <= 1:
                filer = "|".join((nam,url,error,ext,chap_nam,*args))
            else:
                filer = "|".join((nam,url,error,ext,chap_nam))
                filer = filer+ "|" + "|".join(args)
            
            print(filer)
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
                files = f.read()
                files = files.split("\n")
            h = False
            for j, i in enumerate(files):
                if i.split("|")[0] == filer.split("|")[0]:
                    g = input("[modify,leave]: ")
                    h =True 
                    if g.lower() == "m":
                        files[j] = filer
                        print("modefied(%s)"%(filer.split("|")[0]))

            if h == False: files.append(filer); print("added(%s)"%(filer.split("|")[0]))
            files = "\n".join(files)
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","w") as f:
                f.write(files)
    def addin():
        if len(e1.get()) > 2:
            parameter(e1.get())
            for i in q55.winfo_children():
                i.pack(fill= "x",ipadx= 5, side= "top", pady = 5,padx= 5)
            e1.delete(0,tk.END)
            b7.pack_forget()
            l7.pack_forget()
            q7.pack_forget()
            b7.pack(side= "top", padx= 10, anchor= "e")#, fill= "x")
            l7.pack(side= "top",pady= 5 , padx=5)
            q7.pack(side= "top",fill= "both", padx= 5, pady= 5)
    def insertin():
        lc = [] 
        skip = ["","7"]
        for i in q55.winfo_children():
            z = False
            for k in skip:
                z = False
                if i.winfo_name() == "!ctkframe"+k: continue
                z= True
            if z == True:
                for j in i.winfo_children():
                    if j.winfo_name() == "!ctkentry":
                        if j.get() == "": lc = []; break
                        lc.append(j.get())
                        j.delete(0,tk.END)
        olll= "W-Instl"
        if olll in ol:
            olh = ol.index(olll)
            if olh < len(ol)-1:
                validate(*lc[:olh], ids= lc[olh], *lc[olh+1:])
            else:
                validate(*lc[:olh], ids= lc[olh])
        else:
            validate(*lc)
            pass

    b7 = ctk.CTkButton(q5,text="create".upper(), width= 200,command=insertin)
    b7.pack(side= "top", padx= 10, anchor= "e")
    l7 = ctk.CTkLabel(q5, text=f"Add Websites Parameters-[NEW]".center(just_c).upper(), font= ("", 12, "underline","bold"))
    l7.pack(side= "top",pady= 5, padx= 5)
    q7 = ctk.CTkFrame(q5,width= ridt1[1]-10, fg_color= "transparent")
    e1 = ctk.CTkEntry(q7, width= 200)
    e1.pack(side= "left")
    ctk.CTkButton(q7,text="Add",command=addin).pack(side= "right", padx= 2.5)
    q7.pack(side= "top",fill= "both", padx= 5, pady= 5)

    q1.pack(expand= True, fill= "both", padx= 10, pady= 10)

if True: # Browse
    tabview2 = ctk.CTkTabview(w1)
    tabview2.pack(padx=10, pady=10)
    tab11 = tabview2.add("source")
    tab12 = tabview2.add("ext")

    ridt1 = unit(widt, 32, "21/13",pad_div= 0.31)
    q11 = ctk.CTkFrame(tab11, width= 1500, height= 700)
    q11.pack(expand= True, fill= "both", padx= 5, pady= 5)
    
    if True: # source
        ope = False
        if True:
            ty13 = ctk.CTkFrame(q11, height= 700, width= 1500)#width= ridt1[1]-10)
            ty13.place(x=0, y=0)
            ty13.lower()
            ty21 = ctk.CTkFrame(ty13, fg_color= "transparent")
            ty21.grid()

            scrollable_frame22 = ctk.CTkScrollableFrame(ty21, width= 925, height= 380)

            def clear1(event):
                ty13.lower()
                for i in scrollable_frame22.winfo_children(): # improve performance
                    i.destroy()

            c_nam = ctk.CTkLabel(ty21, text="", font= ("", 15, "bold"))
            c_nam.grid(column=0, row=0, sticky="n",columnspan=4)
            x_but = ctk.CTkButton(ty21, font= ("", 15, "bold"), width= 25, height= 20,text="✕")#"❎")
            x_but.grid(column=1, row=0, sticky="e")
            x_but.bind("<Button-1>", clear1)

            scrollable_frame22.grid(columnspan= 2)

            def noves(scrollable_frame2,typ=1):
                gr = 6
                ft = tl.collecter(typ)
                item = len(ft[1].split("|"))
                c_nam.configure(text= ft[0])
                lllo1 = item # batch
                bat = 3

                
                # for i in scrollable_frame22.winfo_children():
                #     i.destroy()

                for i in range(0, lllo1, bat):
                    # Create a batch of widgets
                    batch = (i,i+bat) #showrx[i:i+bat]
                    for j in range(*batch): #item):
                        if j < item:
                            nov(scrollable_frame2,nam= ft[1].split("|")[j], web= ft[0].lower(),ext=lib)
                            pass
                    able = scrollable_frame2.winfo_children()[i:i+bat]
                    for ji1,k in enumerate(able):
                        j = i+ji1
                        k.grid(column=j%gr,row=(j//gr)+1, padx= 5, pady= 5)
        
            def norll(event):
                noves(scrollable_frame22, event)      

        if True:
            ty11 = ctk.CTkFrame(q11, height= 550, width= 1500)
            ty11.place(x=0,y=0)
            ty12 = ctk.CTkFrame(ty11, fg_color= "transparent")
            ty12.grid()

            scrollable_frame12 = ctk.CTkScrollableFrame(ty12, width= 920, height= 405, fg_color= "transparent")

            def noves1(ty1,ty2,scrollable_frame2,typ=0):
                gr = 6
                with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
                    file = f.read()
                    file = file.split("\n")

                for i in range(len(file)):
                    lo = file[i].split("|")
                    txt = f"Rating: {rd.randint(0,5)}/5"
                    n = lo[0]
                    Web(scrollable_frame12,n,txt=txt+" "*(50-len(txt)), ev1= ty1,ev2= ty2,ev3= scrollable_frame2, typ= i, g = norll)

                for j,i in enumerate(scrollable_frame12.winfo_children()):
                    i.grid(column=j%gr,row=(j//gr)+1, padx= 5, pady= 5)
            
            def nnn(event):
                for i in q5.winfo_children():
                    i.pack(fill= "x",ipadx= 5, side= "top")

            noves1(ty13,ty12,scrollable_frame12)

            scrollable_frame12.grid(columnspan= 2, padx= 5, pady= 5)

    w1.pack(expand= True, fill= "both", padx= 10, pady= 10)

if True: # Search # add remove function #fix
    def search():
        for i in q32.winfo_children():
            if i.winfo_name() == "!ctkentry":
                if len(i.get()) > 3:
                    sech(i.get())
        r.focus()
        pass

    q31 = ctk.CTkFrame(tab3, width= 1500, height= 700)
    q31.pack(expand= True, fill= "both", padx= 10, pady= 10)
    q32 = ctk.CTkFrame(q31, width= 1500, fg_color= "transparent")
    q32.pack(fill= "both", padx= 10, pady= 10)
    ctk.CTkEntry(q32, width= 820, placeholder_text= "Search Here! (must be a least 3 letters long)").pack(side= "left", padx= 5, pady= 10)
    ctk.CTkButton(q32,text= "Search", command= search).pack(side= "left", padx= 5, pady= 10)
    q33 = ctk.CTkFrame(q31, width= 1500, fg_color= "transparent")
    q33.pack(fill= "both", padx= 10, pady= 10)

    if True:
        scrollable_frame34 = ctk.CTkScrollableFrame(q33, width= 1150, height= 480, )

        lopp = []
        def sech(term = ""):
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
                file = f.read()
                file = file.split("\n")

            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/sea.txt","r") as f:
                fs = f.read()

            if term != "": # fix the destroy code
                for i in scrollable_frame34.winfo_children():
                    lif = [f"!ctkframe{i+1}" for i in range(len(file))]
                    lif[0] = lif[0][:-1]
                    if i.winfo_name() in lif:
                        for j in i.winfo_children():
                            lif1 = [f"!canvas" for i in range(len(file))]
                            lif1[0] = lif1[0][:-1]
                            if j.winfo_name() in lif1:
                                for k in j.winfo_children():
                                    for k1 in k.winfo_children():
                                        k1.destroy()
            
            if fs == "": fs = 0
            ly1, ly2 = [], []

            if int(fs) != len(file):
                for i in range(int(fs), len(file)):
                    txt = file[i].split("|")[0].capitalize()
                    lopp.append(searc(scrollable_frame34, nam = txt, li = ly1, ly= ly2, ext= lib, theme_c= theme_c, cont= q31, term= term))
            for i in range(len(file)):
                txt = file[i].split("|")[0].capitalize()
                search_word = file[i].split("|")[-1].split("^^")
                search_term = file[i].split("|")[1]+"/"+search_word[0] + term.replace(" ", "+") + search_word[1]
                
                if term != "":
                    li = tl.searched(search_term)
                    ly1 = [i[0] for i in li]
                    ly2 = [i[1] for i in li]
                    lopp[i].doo(ly1, ly2, lib)
            with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/sea.txt","w") as f:
                f.write(str(len(file)))

        sech()
        
        scrollable_frame34.pack(fill= "both",expand= True, padx= 5, pady= 5)
    pass

if True: # Settings
    # q21 = ctk.CTkFrame(tab4, width= 1500, height= 700)
    # q21.pack(expand= True, fill= "both", padx= 10, pady= 10)
    if True:
        scrollable_frame4 = ctk.CTkScrollableFrame(tab4,  width= 1190, height= 600)

        li = ["Confirm Exit", "Theme"]

        def seel():
            for i in scrollable_frame4.winfo_children():
                if i.winfo_name() in ["!ctkcheckbox","!ctkcheckbox2","!ctkcheckbox3"]:
                    if i.cget("text") == "Theme":
                        if i.get() == 1:
                            ctk.set_appearance_mode("light")
                        else:
                            ctk.set_appearance_mode("dark")
                    tl.setters("w", i.cget("text"), i.get())
            pass

        for i in li:
            ctk.CTkCheckBox(scrollable_frame4, text= i, command= seel, 
            variable= tk.IntVar(value= int(tl.setters("r", i)))).pack(pady= 5, anchor= 'w', padx=5)

        if True: # inapporopriate
            def display():
                if int(c1.get()) == 1:
                    g2.pack(pady=5)
                if int(c1.get()) == 0:
                    g2.pack_forget()
                tl.setters("w", c1.cget("text"), c1.get())
            def show():
                for u in g1.winfo_children():
                    if u.winfo_name() == "!ctkentry":
                        lc.append(" "+u.get())
                        tl.errors(val=u.get(),md= "a")
                        u.delete(0,tk.END)
                        r.focus()
                        
                lc1 = "["+",".join(lc)+"]"
                for u in g2.winfo_children():
                    if u.winfo_name() == "!ctklabel":
                        u.configure(text = lc1)
                pass
            def show2():
                for u in g7.winfo_children():
                    if u.winfo_name() == "!ctkentry":
                        # lc.append(u.get())
                        u.pack(anchor= "w", side= "left", padx=5)
                        #lc1 = "["+",".join(lc)+"]"
                        if u.get() != "":
                            if u.get().isdecimal():
                                if int(u.get()) <= len(lc):
                                    lc.pop(int(u.get()))
                                    lc1 = "["+",".join(lc)+"]"
                            tl.errors(val= u.get(),md="d")
                            lc11 = [i.strip() for i in lc]
                            if u.get() in lc11: lc.pop(lc11.index(u.get()))
                            lc1 = "["+",".join(lc)+"]"
                            u.delete(0,tk.END)
                            r.focus()
                            u.pack_forget()
                        else:
                            return None
                for u in g2.winfo_children():
                    if u.winfo_name() == "!ctklabel":
                        u.configure(text = lc1)
                pass

            lc = tl.errors()
            #print(lc)
            lc1 = "["+",".join(lc)+"]"
            g = ctk.CTkFrame(scrollable_frame4, fg_color= "transparent")
            g.pack(pady=5, padx= 5, anchor="w")
            c1 = ctk.CTkCheckBox(g, text= "Inappropriate", command= display,variable= tk.IntVar(value= int(tl.setters("r", "Inappropriate"))))
            c1.pack(anchor= 'w', pady= 5)
            g2 = ctk.CTkFrame(g, fg_color= "transparent")

            if int(tl.setters("r", "Inappropriate")) == True: display()

            g1 = ctk.CTkFrame(g2, fg_color= "transparent")
            g1.pack(pady=5,anchor= "w")
            ctk.CTkEntry(g1,placeholder_text= "Add inapropriate words", width= 200).pack(anchor= "w", side= "left")
            ctk.CTkButton(g1,text= "ADD", width= 100, command= show).pack(anchor="w", side= "left", padx=5)

            g7 = ctk.CTkFrame(g2, fg_color= "transparent")
            g7.pack(pady=5, anchor= "w")
            ctk.CTkButton(g7,text= "DELETE", width= 100, command= show2).pack(anchor= "w", side= "left")
            ctk.CTkEntry(g7,placeholder_text= "Remove inapropriate words", width= 200)
            ctk.CTkLabel(g2,text=lc1, wraplength= 800, justify= "left").pack(anchor= 'w')

        if True: # copywrite
            def display1():
                if int(c2.get()) == 1:
                    g4.pack(pady=5)
                if int(c2.get()) == 0:
                    g4.pack_forget()
                tl.setters("w", c2.cget("text"), c2.get())
            def show1():
                for u in g3.winfo_children():
                    if u.winfo_name() == "!ctkentry":
                        lc2.append(u.get())
                        tl.errors(1,u.get(),"a")
                        u.delete(0,tk.END)
                        r.focus()
                        
                lc3 = "["+", ".join(lc2)+"]"
                for u in g4.winfo_children():
                    if u.winfo_name() == "!ctklabel":
                        u.configure(text = lc3)
                pass
            
            lc2 = tl.errors(1)
            lc3 = "["+",".join(lc2)+"]"
            g5 = ctk.CTkFrame(scrollable_frame4, fg_color= "transparent")
            g5.pack(pady=5, padx= 5, anchor= "w")
            c2 = ctk.CTkCheckBox(g5, text= "Copywrited", command= display1,variable= tk.IntVar(value= int(tl.setters("r", "Copywrited"))))
            c2.pack(anchor= 'w', pady= 5)
            g4 = ctk.CTkFrame(g5, fg_color= "transparent")
            if int(tl.setters("r", "Copywrited")) == True: display1()

            g3 = ctk.CTkFrame(g4, fg_color= "transparent")
            g3.pack(pady=5,anchor= "w")
            ctk.CTkEntry(g3,placeholder_text= "Add copywrited words", width= 200).pack(anchor= "w", side= "left")
            ctk.CTkButton(g3,text= "ADD", width= 100, command= show1).pack(side= "left", padx=5)
            ctk.CTkLabel(g4,text=lc3).pack(anchor= 'w')
            pass

        ctk.CTkCheckBox(scrollable_frame4, text= "Clone", command= seel,
        variable= tk.IntVar(value= int(tl.setters("r", "Clone")))).pack(pady= 5, anchor= 'w', padx=5)

        scrollable_frame4.pack(fill= "both",expand= True, padx= 5, pady= 5)

if True: # Update # fix the placement # fix the missing updates problem # fix network issue # make the update lowest to highest
    ctk.CTkButton(tab6, text="↺", command= reload).pack(pady= 2.5)#anchor= "e")
    scrollable_frame6 = ctk.CTkScrollableFrame(tab6,  width= 1212, height= 600)

    class Hist():
        def __init__(self, u, nam,typ= "log") -> None:
            self.u = u

            if typ == "log":
                image1 = Image.open("C:/Users/ajuga/OneDrive/Desktop/test/nec3.jpg")

                new_width  = 100
                new_height = 100
                img = image1.resize((new_width, new_height), Image.Resampling.LANCZOS)

                r1 = ctk.CTkFrame(master=self.u,fg_color= "transparent")
                r1.pack()

                r2 = ctk.CTkFrame(master=r1, width= 50, height= 10, fg_color= "transparent")
                r2.pack(fill= "both", side= "left")

                divd = 2.3
                imgs = ctk.CTkImage(dark_image= img, size= (round(new_width/divd),round(new_height)/divd))
                ctk.CTkLabel(master= r2,image=imgs,text= "").pack(padx= 5,pady=2.5,anchor='center')

                r4 = ctk.CTkFrame(r1,fg_color= "transparent")
                r4.pack(fill= "both",padx= 5, pady= 12,side= "left")

                lab1 = ctk.CTkLabel(r4,text= (f"{nam}".capitalize()),
                font= ("TkDefaultFont",12,"bold"),width= 480, anchor= "w",height= 10, justify= "left")
                lab1.pack(fill= "x",padx= 5)
            else:
                r1 = ctk.CTkFrame(master=self.u,fg_color= "transparent")
                r1.pack(anchor= "w", fill="x", expand= True)
                lab1 = ctk.CTkLabel(r1,text= (f"{nam}".capitalize()),
                font= ("TkDefaultFont",15,"bold"), width= 960, anchor= "w",height= 10, justify= "left")
                lab1.pack(fill= "x",padx= 5, expand= True)
            pass

    linn = [["Today", ""],["web","love","log"],["webbb","lovvve","log"],["yesterday",""],["webb3b","lvvvovvve","log"]]

    with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/logg.txt","r") as f:
            loo = f.read()
    popp = []
    reqim = 10
    for iio in loo.split("\n"): #add date time
        if len(iio.split("\p")) > 1:
            if len(iio.split("\p")[1].split("|")) > reqim: reqim = len(iio.split("\p")[1].split("|"))
            for oio in iio.split("\p")[1].split("|")[-reqim:]: # fix length error
                popp.append([oio + " added", iio.split("\p")[0], "log"])
        else:
            popp.append([yes_tod(iio), ""])
    
    for hh in popp:
        if len(hh) == 3:
            Hist(scrollable_frame6, "\n".join(hh[:2]), hh[2])
        else:
            Hist(scrollable_frame6, hh[0], hh[1])
    
    for it in scrollable_frame6.winfo_children():
        it.pack(fill= "x", expand=True)

    scrollable_frame6.pack(side="right", fill="both", expand=True, ipadx= 2.5, pady = 5)

if True: #total getter
    network = net_check("https://www.google.com")

    with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt","r") as f:
        files = f.read()
        files = files.split("\n")
    with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
        files12 = f.read()
        files12 = files12.split("\n")
    showrx= [nnnn.split("|")[:2] for nnnn in files]
    for v,i in enumerate(showrx):
        f = showrx[v]
        f1 = ""
        for j in files12:
            if i[1] == j.split("|")[0]:
                f = j.split("|")[1].replace("https://", "") + j.split("|")[3].replace("https://", "")[:-1]
                if i[1] not in ["novelbin"]:
                    f1 = j.split("|")[2]
                break
        showrx[v][1] = f
        showrx[v][0] = i[0].replace(" ","-").lower()
        showrx[v].append(f1)

    def tot_bat_thr():
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_fm.txt","r") as f2:
            pr = f2.read()
            if len(pr) > 0:
                frxc = int(pr)
            else: frxc = 0
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_bat.txt","r") as f:
            tb = [[j.split("|") for j in i.split("\p")] for i in f.read().split("\n")]
        lllo = len(showrx)
        if frxc < lllo:
            bat = 2
            for i in range(frxc, frxc+bat, bat):
                if i < lllo:
                    # Create a batch of widgets
                    batch = showrx[i:i+bat]
                    if batch in tb:
                        continue
                    #print(batch)
                    
                    threads = [threading.Thread(target=total_get, args=(p, w, m), name= p+"|"+w) for p,w,m in batch]

                    for thread in threads:
                        thread.start()
            
                    with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_bat.txt","w") as f:
                        if type(tb) == list:
                            if len(tb[0][0][0]) == 0:
                                #write directly
                                f.write("\p".join(["|".join(i) for i in batch]))
                                pass
                            else:
                                #appennd
                                tb.append(batch)
                                f.write("\n".join(["\p".join(["|".join(j) for j in im]) for im in tb]))
                
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_fm.txt","w") as f:
                # print(str((frxc+bat)), frxc, bat)
                f.write(str(frxc+bat))
           
            #r.after(5000, tot_bat_thr)
        else:
            # with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_fm.txt","w") as f:
            #     f.write(str(0))
            savv(0, "True")
            #add reset code
            pass

    def updt():
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_fm.txt","r") as f2:
            pr = f2.read()
            if len(pr) > 0:
                frxc = int(pr)
            else: frxc = 0
        with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/tot_bat.txt","r") as f:
            tb = [[j.split("|") for j in i.split("\p")] for i in f.read().split("\n")]
        tbl = []
        for nin in tb:
            for iin in ["|".join(nin1[:2]) for nin1 in nin]:
                tbl.append(iin)
        lllo = len(showrx)
        diffr = False
        if frxc < lllo:
            for thread in threading.enumerate():
                diffr = False
                # print(thread.name, thread.name not in tbl)
                #if len(threading.enumerate()) > 1: #fix this
                #if "Thread" not in thread.name:
                if thread.name not in tbl:
                    diffr = True
            if diffr:
                tot_bat_thr()
                thr = r.after(1000, updt) # adjust
                savv(1,thr)  
            else:
                thr = r.after(10000, updt) # adjust
                savv(1,thr)

    def savv(num= 0, val="", f= "w"):
        if f == "w":
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/comp.txt","r") as f:
                thr = f.read().split("|")
            thr[num] = val
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/comp.txt","w") as f:
                f.write("|".join(thr))
        else:
            with open(f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/comp.txt","r") as f:
                thr = f.read().split("|")
            return thr[num]

   
    def main(r):
        if True:#network and False:
            updt()
            pass
        tLoad()
        r.protocol("WM_DELETE_WINDOW", on_closing)
        r.mainloop()
       
main(r)




if False: #batching
    import tkinter as tk

    # Create the main window
    root = tk.Tk()

    # Set the number of widgets to load at a time
    batch_size = 50

    # Create a list of widgets to load
    widgets = [tk.Button(root, text=f"Button {i}") for i in range(500)]

    # Load the widgets in batches
    for i in range(0, len(widgets), batch_size):
        # Create a batch of widgets
        batch = widgets[i:i+batch_size]
        
        # Add the widgets to the main window
        for widget in batch:
            widget.pack()
        
        # Update the display to show the newly added widgets
        root.update()

    # Start the main loop
    root.mainloop()
