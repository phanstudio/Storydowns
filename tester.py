import random as rd
import requests as req
from gtts import gTTS
from pathlib import Path
import time,bs4, os, pyttsx3, webbrowser, asyncio
from threading import Thread
from tools import Tools as tl
# from playwright.async_api import async_playwright


pop = False

home = "C:/Users/ajuga/OneDrive/Desktop/test"

def store(web= "novelhard",nam= "i-hate-systems",total=100,li_of_chap= "0-10,67,70-77,99", tim = "00:00"):
    filer = "|".join((nam,str(total),li_of_chap,tim))
    url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/input\{web}.txt"
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
                #print("modefied(%s)"%(filer.split("|")[0]))

    if h == False: files.append(filer); print("added(%s)"%(filer.split("|")[0]))
    if new == True: files = files[1:]
    files = "\n".join(files)

    with open(url,"w") as f:
        f.write(files)

def converter(y= []):
    # check for decimals
    li = list(map(int,y.split(",")))
    l = 0
    lu = []
    for t in li:
        if l != 0:
            l -= 1
            if l < 0: l=0
            continue
        o = t
        while True:
            if o+1 in li:
                o += 1
            else:
                l = o - t
                break
        if l == 0:
            lu.append(t)
        else:
            lu.append([t,t+l])  
    lt = []
    for h in lu:
        if type(h) == list:
            lt.append(f"{h[0]}-{h[1]}")
            continue
        lt.append(str(h))
        
    return ",".join(lt)

def digit_checker(f=[]):
    f1 = f
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
    return f1

def collect(web= "novelhard",nam= "i-hate-systems"):

    url= f"C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/input\{web}.txt"
    # add a create func for multiple websites

    with open(url,"r") as f:
        files = f.read()
        files = files.split("\n")

    if files != "":
        for j, i in enumerate(files):
            if i.split("|")[0] == nam:    
                return i.split("|")#[0],i.split("|")[1]

def logger(new_num=1,old_num="0,0,0,0"):
    new = False
    if old_num == "0,0,0,0"or old_num == "": new = True
    if new == False:
        f1 = old_num.split(",")
        f1 = digit_checker(f1)
        p = set(f1)
        p.add(str(new_num))
        y = list(p)
        y = list(map(int,y))
        y.sort() #sort properly
        y = list(map(str,y))
        y1 = ",".join(y)
        y1 = converter(y1)
    else:
        y1 = str(new_num)
    return y1

def loggs(num1=50, web="you", nov="your", tim= 30):
    log = ""
    times = []
    files = tl.collect(web, nov)
    #print(files)
    if files != None: log = files[2]; times = files[3].split(",")
    if files[2] == "0,0,0,0": times = []
    tim = hex(tim)[2:]
    log = logger(num1,log)
    times.append(str(tim))
    y = (web,nov,200,log,",".join(times))
    # fix space problem
    tl.store(y[0],y[1],y[2],y[3],y[4])

def sav(d):
    with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/networking/sav.txt", "w", encoding= "utf-8") as f:
        print(d)
        d1 = "".join(d)
        if d1 != "":
            d = "\n".join(d)
            f.write(d)
            raise ValueError()

# async def main():
#     async with async_playwright() as p:
#         for browser_type in [p.chromium, p.firefox, p.webkit]:
#             #async with browser_type.launch() as browser:
#             browser = await browser_type.launch()
#             page = await browser.new_page()
#             await page.goto("https://freewebnovel.com/son-of-the-hero-king/chapter-1.html")
#             sav(await page.locator("p").all_text_contents())

class Downs(Thread):
    def __init__(self,nums = "8-10",url="i-hate-systems",web = "novelhard",val="", prog="", lab= "",err="", gen=""):
        super().__init__()
        self.numx = nums
        self.url = url
        self.web = web
        self.vrr = val
        self.prog = prog
        self.lab = lab
        self.k = ""
        self.err = err
        self.genr = gen

        if "-" in nums: self.numx = nums.split("-")
        else: self.numx = nums
        if type(self.numx) == list:
            self.numx[0] = int(self.numx[0])
            self.numx[1] = int(self.numx[1])

    def run(self) -> None:
        self.chapter_creator1(numb=self.numx,web = self.web,url=self.url, gen= self.genr,rw=True)
        pass
        #return super().run()
        pass

    def chapter_creator1(self,select= "p",numb="2-9", web = "novelhard", url= "i-hate-systems", create= False, rw = False, gen= "male", lr= ""):
        if type(numb) == int or type(numb) == str: numb = [int(numb), int(numb)]
        for num in range(numb[0], numb[1]+1):
            self.prog.set(0)
            web = self.vrr.nums[1]
            url = self.vrr.nums[0] #check

            if num in list(map(int,tl.digit_checker(tl.collect(web,url)[2].split(",")))): continue#print(num)
            self.lab(num)
            h = self.url_getter(web,url,num)
            text= self.corrector(h)
            #print(text)

            if True: #create path
                p = Path(home) / url
                if (p).exists() == False: p.mkdir()
                if create == False and (p/("chapter%s.wav"%(num))).exists() == True: self.prog.set(1);continue
                else: create = True
                folder = url

            # add time codes and find duration
            if (create == True or rw == True):
                engine = pyttsx3.init()
                voices =  engine.getProperty("voices")
                if gen ==  voices[0].name:
                    engine.setProperty("voice", voices[0].id)
                    engine.setProperty("rate", 214)
                else:
                    for i in voices:
                        if gen == i.name:
                            engine.setProperty("voice", i.id)
                            break
                #print(home + "/" +folder + "/" + "chapter%s.wav"%(num))
                if True:
                    engine.save_to_file(text, (home + "/" +folder + "/" + "chapter%s.wav"%(num)))
                    engine.runAndWait()
                    #print("Chapter"+ str(num)+ " download Done")
            if True:
                #print(tl.collect(self.vrr.nums[1],self.vrr.nums[0]))
                dur = rd.randint(60, 240)
                loggs(num,web,url,dur)
                self.vrr.update(tl.collect(self.vrr.nums[1],self.vrr.nums[0]), int(tl.read(url)[2]), num)
                self.lab(num)

                # val = self.prog.get()
                # for _ in range(40):
                #     val += 0.025
                #     self.prog.set(val)
                #     if self.prog.get() == 1:
                #         break
                self.prog.set(1)
                time.sleep(0.5)
                #print("Done!")
        pass
    
    def url_getter(self,web,book="i-hate-systems",num= 1):
        lr = "/"
        info = self.reads(web)
        urlx = info[1]+info[3]+book.replace(" ","-").replace(":","").lower()+"/"+info[4]+str(num)+lr
        #webbrowser.open(urlx) # for testing
        # try:
        #     asyncio.run(main())
        # except:
        #     print("fin")
        # add sessions
        for _ in range(5):
            try:
                res = req.get(urlx)
                break
            except req.exceptions.RequestException as e:  # This is the correct syntax
                self.err()
                raise SystemExit(e)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        return soup.select("p")
   
    def corrector(self,h):
        with open(r"C:\Users\ajuga\OneDrive\Documents\Jupiter-python-try\learn\TkinteR\Storydowns\storage\erros.txt") as f1:
            file = f1.read()
        li = [i.get_text().strip("\r") for i in h] 
        if int(tl.setters("r", "Clone")) == 1:
            l_fac =len(li[0]) 
            if l_fac > 30:
                l_fac = 30
            
            if len(li) > 4:
                for i in range(1,6):
                    if li[i] != "":
                        if len(li[i]) >= l_fac:
                            if "chapter" in li[0][:30].lower():
                                slz = li[0][:100].split("  ")
                                slz1 = slz = len(slz[0])+1
                            else: 
                                slz = -1
                                slz1 = 0
                            if li[0][slz1:slz+l_fac] == li[i][:l_fac]:
                                li = li[:i]
                                break
                for _ in range(30):
                    try:
                        li.remove("")
                    except:
                        break
                #h = li
        text = "\n".join(li)
        if int(tl.setters("r", "Inappropriate")) == 1:
            filer = file.split("\n/c/\n")[0].split(":")[1].split(",")
            filer = [j.strip() for j in filer]
            # li = []
            # for p in h:
            #     i = p.get_text()
            #     i = i.strip("\r")
            #     li.append(i)
            text = "\n".join(li)
            lk = ["a","e","o","i","u"]
            for k in filer:
                k1 = k
                for j in lk:
                    k1 = k1.replace(j, "*")

                text = text.replace(" "+k, " "+k1).replace(" "+k.capitalize(), " "+k1.capitalize()).replace(" "+k+"s", " "+k1+"s")
                t1 = text.split(" ")
                for ll,it in enumerate(t1):
                    if k == it:
                        t1[ll] = k1
                
                text = " ".join(t1)
            if int(tl.setters("r", "Copywrited")) == 1:
                lc = []
                filerr = file.split("\n/c/\n")[1].split(":")[1].split(",")
                filerr = [j.strip() for j in filerr]
                filerr.append("@")
                filess = text.split("\n")
                for p in filess:
                    if not any(item in p for item in filerr):
                        lc.append(p)
                text = "\n".join(lc)
        elif int(tl.setters("r", "Copywrited")) == 1:
            lc = []
            filer = file.split("\n/c/\n")[1].split(":")[1].split(",")
            filer = [j.strip() for j in filer]
            filer.append("@")
            # for p in h:
            #     i = p.get_text()
            if not any(item in li for item in filer):
                lc.append(li)
            text = "\n".join(lc)

        return text

    def reads(self,web):
        with open("C:/Users/ajuga/OneDrive/Documents/Jupiter-python-try/learn/TkinteR/Storydowns/storage/webfile.txt","r") as f:
            files = f.read()
            files = files.split("\n")

        for j, i in enumerate(files):
            if i.split("|")[0] == web:
                return i.split("|")

