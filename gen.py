import tkinter as tk
import tkinter.ttk
from PIL import Image,ImageTk
import app,setting

class Gen:
    def __init__(self, getCmds,dev=False):
        
        # set
        self.getCmds = getCmds
        
        if(not dev):
            # making app
            self.root = tk.Tk()
            self.root.resizable(0,0)
            self.root.title("ameDesktop")
            
            # setting slidebar
            self.genNum = tk.IntVar(name = "genNum")
            self.slideBar = tk.Scale(self.root,name="genNumber",variable=self.genNum,length=200,from_=1,to=10,orient=tk.HORIZONTAL)
            self.slideBar.set(3)
            self.slideBar.pack()
            
            # annoy level
            annoyLevels = ("comfy","ame","SMOL AME")
            self.combobox=tkinter.ttk.Combobox(self.root, state="readonly",height=15, values=annoyLevels)
            self.combobox.current(1)
            self.combobox.pack()
            
            # setting button
            self.genButton = tk.Button(self.root,text="generate!",command=self.runAmes)
            self.genButton.pack()
            
            # set icon
            icon = Image.open("ame/ameicon.ico")
            self.root.wm_iconphoto(False, ImageTk.PhotoImage(image=icon))
            
            self.root.mainloop()
        else:
            app.App(3,self.getCmds)
        
    def setSetting(self):
        annoyLev = self.combobox.get()
        if(annoyLev == "ame"):
            setting.main.disruptRate = (1/120)* 100
            setting.main.runRate = 70
            
        if(annoyLev == "comfy"):
            setting.main.disruptRate = (1/240)* 100
            setting.main.runRate = 35
            
        if(annoyLev == "SMOL AME"):
            setting.main.disruptRate = (1/30)* 100
            setting.main.runRate = 140
        
    def runAmes(self):
        
        self.setSetting()
        
        self.root.destroy()
        app.App(self.genNum.get(),self.getCmds)