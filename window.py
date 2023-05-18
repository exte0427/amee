import tkinter as tk
from PIL import ImageTk
import random
import fun,setting

from win32api import GetMonitorInfo, MonitorFromPoint

class Window:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.resizable(False, False)
        self.root.title("ame")
        
        self.root.wm_attributes("-topmost", True)
        
        self._locate((0,0))
        
    def _locate(self,targetPos):
        self.pos = targetPos
        self.root.geometry(f'+{int(targetPos[0])}+{int(targetPos[1])}')
    
    def delThis(self,event):
        self.root.destroy()
        
    def _setImg(self,rawImg):
        img = ImageTk.PhotoImage(rawImg)
        imgLabel = tk.Label(self.root,image = img,cursor="hand1")
        imgLabel.image = img
        imgLabel.configure(image=img)
        imgLabel.bind("<Button-1>",self.delThis)
        imgLabel.pack()
        
        self.size = (self.root.winfo_width(),self.root.winfo_height())

        self.root.update_idletasks()
        
    def _getEdge(self):
        
        rootSize = self.root.winfo_width(), self.root.winfo_height()
        print(rootSize)
        if(fun.percent(50)):
            if(fun.percent(50)):
                # top
                return (-random.randint(0,rootSize[0]),0)
            else:
                # bottom
                return (-random.randint(0,rootSize[0]),-rootSize[1])
        else:
            if(fun.percent(50)):
                # left
                return (0,-random.randint(0,rootSize[1]))
            else:
                # right
                return (-rootSize[0],-random.randint(0,rootSize[1]))
    
def getTask():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    return monitor_area[3]-work_area[3]

taskSize = -1
def randomPos(rootSize = None):
    global taskSize
    if taskSize == -1:
        taskSize = getTask()
    
    winSize = setting.main.screenSize
    
    if(rootSize == None):
        rootSize = setting.main.appSize
    
    return (random.randint(0,winSize[0]-rootSize[0]),random.randint(0,winSize[1]-rootSize[1]-taskSize))

def randomEdge(rootSize = None):
    
    winSize = setting.main.screenSize
    
    if(rootSize == None):
        rootSize = setting.main.appSize
    
    if(fun.percent(50)):
        if(fun.percent(50)):
            # left
            return (-rootSize[0],random.randint(0,winSize[1]-rootSize[1]))
        else:
            # right
            return (winSize[0],random.randint(0,winSize[1]-rootSize[1]))
    else:
        if(fun.percent(50)):
            # top
            return (random.randint(0,winSize[0]-rootSize[0]),-rootSize[1])
        else:
            # bottom
            return (random.randint(0,winSize[0]-rootSize[0]),winSize[1])