import tkinter as tk
from PIL import Image,ImageTk
import ame

class Gen:
    def __init__(self, getCmds,config):
        self.root = tk.Tk()
        self.root.title("ameDesktop")
        
        # setting slidebar
        self.genNum = tk.IntVar(name = "genNum")
        self.slideBar = tk.Scale(self.root,name="genNumber",variable=self.genNum,length=200,from_=1,to=10,orient=tk.HORIZONTAL)
        self.slideBar.pack()
        
        # set
        self.getCmds = getCmds
        self.config = config
        
        # setting button
        self.genButton = tk.Button(self.root,text="generate!",command=self.runAmes)
        self.genButton.pack()
        
        # set icon
        icon = Image.open("ame/ameicon.ico")
        self.root.wm_iconphoto(False, ImageTk.PhotoImage(image=icon))
        
        self.root.mainloop()
        
    def runAmes(self):
        # del
        self.root.destroy()
        
        mainAme = ame.Run(self.getCmds,self.config,True)
        for _ in range(self.genNum.get()-1):
            ame.Run(self.getCmds,self.config,False)
            
        # run main ame
        mainAme.root.mainloop()