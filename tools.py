import requests as req
import bs4, os
from tkinter import ttk

class Tools():
    @classmethod
    def store(cls,web= "novelhard",nam= "i-hate-systems",total=100,li_of_chap= "0-10,67,70-77,99", tim = "00:00"):
        filer = "|".join((nam,str(total),li_of_chap,tim))
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/websites/{web}.txt"
        # add a create func for multiple websites

        new = False
        if os.path.exists(url) == False:
            new = True
            with open(url,"w") as f:
                f.write("")

        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")

        h = False
        if files != "":
            for j, i in enumerate(files):
                if i.split("|")[0] == filer.split("|")[0]:
                    h =True 
                    files[j] = filer
                    print("modefied(%s)"%(filer.split("|")[0]))

        if h == False: files.append(filer); print("added(%s)"%(filer.split("|")[0]))
        if new == True: files = files[1:]
        files = "\n".join(files)

        with open(url,"w") as f:
            f.write(files)

    @classmethod
    def collect(cls,web= "novelhard",nam= "i-hate-systems"):
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/websites/{web}.txt"
        # add a create func for multiple websites
        isExist = os.path.exists(url)
        if isExist == True:
            with open(url,"r") as f:
                files = f.read()
                files = files.split("\n")

            new = False
            for ht in files:
                if ht.split("|")[0] == nam:
                    new = True
            if new == True:
                if files != "":
                    for j, i in enumerate(files):
                        if i.split("|")[0] == nam:
                            if len(i.split("|")) < 3: return i.split("|")[0],i.split("|")[1],"0,0,0,0","0"
                            return i.split("|")
            else: return "","100","0,0,0,0","0"
        else:
            return "","100","0,0,0,0","0"

    @classmethod
    def digit_checker(cls,f=[]):
        f1 = f
        #if f1 != '0':
        i3 = [[]]
        for i in f1:
            if "-" in i:
                i3[0].append(i)
                i1 = i.split("-")
                i2 = []
                for j in range(int(i1[0]),int(i1[1])+1):
                    i2.append(str(j))
                i3.append(i2)
        for i in i3[0]:
            f1.remove(i)
        for j in i3[1:]:
            f1.extend(j)
        y = list(map(int,f1))
        y.sort() #sort properly
        f1 = list(map(str,y))
        #else: f1 =['0']
        return f1

    @classmethod
    def time_converter(cls,z):
        p= int(z,16)
        g= p//60
        k = p - (g * 60)
        if g < 10: g = "0"+str(g)
        if k < 10: k = "0"+str(k)
        m = "%s:%s"%(g,k)
        return m

    @classmethod
    def add(cls,web= "novelhard",nam= "i-hate-systems",total=100):
        filer = "|".join((nam,web,str(total)))
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage\libary.txt"
        # add a create func for multiple websites

        new = False
        if os.path.exists(url) == False:
            new = True
            with open(url,"w") as f:
                f.write("")

        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")

        h = False
        if files != "":
            for j, i in enumerate(files):
                if i.split("|")[0] == filer.split("|")[0]:
                    h =True 
                    files[j] = filer
                    print("modefied(%s)"%(filer.split("|")[0]))

        if h == False: files.append(filer); print("added(%s)"%(filer.split("|")[0]))
        if new == True: files = files[1:]
        files = "\n".join(files)

        with open(url,"w") as f:
            f.write(files)
    
    @classmethod
    def read(cls,num= 0):
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/libary.txt"

        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")
        if type(num) != str:
            return files[num].split("|")
        else:
            for j,i in enumerate(files):
                if num == i.split("|")[0]:
                    return files[j].split("|")
    
    @classmethod
    def inform(cls,li=[], op= "w"):
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/inf.txt"
        if op == "w":
            with open(url,"w") as f:
                f.write("|".join(li))
        else:
            with open(url,"r") as f:
                return f.read().split("|")
    
    @classmethod
    def installer(cls,url = "https://novelbin.net",bll="h3>"):
        #url = "https://novelhard.com" # "https://novelroom.net"
        res = req.get(url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        h = soup.select(bll+"a")#".page-listing-item a")
        single = True
        li = []
        for i in range(len(h)):
            if h[i].get_attribute_list("title")[0] != None:
                if single == False:
                    hb = h[i].select("img")[0].get_attribute_list("data-src")[0]
                    if hb != None:
                        li.append([h[i].get_attribute_list("title")[0],hb])
                else:
                    ll = h[i].get_attribute_list("title")[0]
                    if 'ago' in ll.split() and ("hour" in ll.split() or "hours" in ll.split() or "days" in ll.split() or "day" in ll.split()):
                        pass
                    else:
                        li.append(ll)

        if single == False:
            # img_data = requests.get(li[0][1]).content
            # print(f'{li[0][0]}.jpg')
            # with open(f'{li[0][0]}.jpg', 'wb') as handler:
            #     handler.write(img_data)
            pass
        print(li)
        rl = url.strip("https://").split(".")[0].capitalize()
        cls.adder(rl,li)

    @classmethod
    def adder(cls,web= "novelhard",li=[]):
        filer = "|".join(li)
        filer = web + ":" + filer
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/installed.txt"
        # add a create func for multiple websites
        
        new = False
        if os.path.exists(url) == False:
            new = True
            with open(url,"w") as f:
                f.write("")

        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")

        h = False
        if files != "":
            for j, i in enumerate(files):
                if i.split(":")[0] == filer.split(":")[0]:
                    h =True 
                    files[j] = filer
                    print("modefied(%s)"%(filer.split(":")[0]))
        if files == [""]: files = [filer]
        elif h == False: files.append(filer); print("added(%s)"%(filer.split(":")[0]))
        if new == True: files = files[1:]
        files = "\n".join(files)

        with open(url,"w") as f:
            f.write(files)

    @classmethod
    def collecter(cls,num):
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/installed.txt"
        with open(url,"r") as f:
            files = f.read()
            files = files.split("\n")
        fl = files[num].split(":")
        return fl[0],":".join(fl[1:])


    @classmethod
    def img_read(cls,nam,num=5):
        url=f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/images(book)/{nam}.png"
        if os.path.exists(url) == False: nam = f"No Image/{num}"
        url=f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/images(book)/{nam}.png"
        return url

    @classmethod
    def searched(cls,url):
        #url = "https://novelbin.net/search?keyword=shad"
        res = req.get(url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        h = soup.select("h3>a")
        li = []
        for i in h:
            li.append([i.get_text(),
            i.get_attribute_list("href")[0]])
        return li
    
    @classmethod
    def setters(cls,rw= "r", nam= "", info= ""):
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/sett.txt"
        with open(url,"r") as f:
            filer = f.read().split("\n")
        names = [i.split(":")[0] for i in filer]
        #print(nam, names) debugging
        if nam != "" and nam in names:#
            fill = []
            for i in filer:
                f = i
                if i.split(":")[0] == nam:
                    if rw == "r":
                        return i.split(":")[1].strip(" ")
                    if rw == "w"and info != "":
                        f = [i.split(":")[:1][0],str(info)]
                        f = ": ".join(f)
                    else:
                        print("Set the Value")
                fill.append(f)
            #print(fill, filer, sep= "\n")
            filer = fill
        else:
            print("Parameter is incorrect")
        with open(url,"w") as f:
            f.write("\n".join(filer))

    @classmethod
    def errors(cls,num= 0, val="sex", md= "r"):
        url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/erros.txt"
        nam = ["inapp", "copy"]
        with open(url,"r") as f:
            filer = f.read().split("\n/c/\n")
            flli = []
        for i in filer:
            f =i
            if i.split(":")[0] == nam[num]: #delete
                fii =i.split(":")[1].split(",")
                fi = [j.strip() for j in fii]
                if val in fi:
                    if md == "d":
                        fx = fi.index(val)
                        fii.pop(fx)
                        f = ":".join((i.split(":")[0],",".join(fii)))
                if md == "a":
                    if val not in fi:
                        fii.append(" "+val)
                        f = ":".join((i.split(":")[0],",".join(fii)))
                if md == "r":
                    return fii 
            flli.append(f)
        filer = flli
        with open(url,"w") as f:
            f.write("\n/c/\n".join(filer))
        pass

