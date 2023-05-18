import tkinter as tk
from PIL import ImageTk,Image
import ame,draw,setting

class App:
    def __init__(self,ameNum,getCmds):

        # set app and fullscreen
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        
        # transparent
        self.root.wm_attributes('-transparentcolor','green')
        
        # canvas setting
        self.canvas = tk.Canvas(self.root, bg="green",highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.root.update()
        
        # setting config.setting
        setting.main.screenSize = self.canvas.winfo_width(),self.canvas.winfo_height()
        
        # ameList
        self.ameList = []
        for _ in range(ameNum):
            self.ameList.append(ame.Ame(getCmds))
            
        # managers
        self.drawManager = draw.DrawManager(self)
        
        # start!
        self.nextFrame()
        
        # main loop
        self.root.mainloop()
    
    def nextFrame(self):
        
        for ame in self.ameList:
            ame.nextFrame()
        self.drawManager.nextFrame()
        
        self.root.after(int(1000/setting.main.frameRate),self.nextFrame)