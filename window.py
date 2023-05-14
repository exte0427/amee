import tkinter as tk
from PIL import Image,ImageTk
import random
import getweb,draw,fun

from win32api import GetMonitorInfo, MonitorFromPoint

class Window:
    def __init__(self):
        self.root = tk.Toplevel()
        self._locate((0,0))
        
    def _locate(self,targetPos):
        self.root.geometry(f'+{int(targetPos[0])}+{int(targetPos[1])}')
        
    def _setImg(self,rawImg):
        img = ImageTk.PhotoImage(rawImg)
        imgLabel = tk.Label(self.root,image = img)
        imgLabel.image = img
        imgLabel.configure(image=img)
        imgLabel.pack()

        self.root.update_idletasks()
    
def getTask():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    return monitor_area[3]-work_area[3]

taskSize = -1
def randomPos(root):
    global taskSize
    if taskSize == -1:
        taskSize = getTask()
    
    winSize = root.winfo_screenwidth(), root.winfo_screenheight()
    rootSize = root.winfo_width(), root.winfo_height()
    
    return (random.randint(0,winSize[0]-rootSize[0]),random.randint(0,winSize[1]-rootSize[1]-taskSize))

def randomEdge(root):
    winSize = root.winfo_screenwidth(), root.winfo_screenheight()
    rootSize = root.winfo_width(), root.winfo_height()
    
    if(fun.percent(50)):
        if(fun.percent(50)):
            # left
            return (-rootSize[0],random.randint(0,winSize[1]-rootSize[1]))
        else:
            # right
            return (winSize[1],random.randint(0,winSize[1]-rootSize[1]))
    else:
        if(fun.percent(50)):
            # top
            return (random.randint(0,winSize[0]-rootSize[0]),-rootSize[1])
        else:
            # bottom
            return (random.randint(0,winSize[0]-rootSize[0]),winSize[1])

def _test():
    
    rawImg = getweb.getImg("https://pbs.twimg.com/media/Eomn0n5W8AAZu0K.png")
    rootImg = rawImg
    
    main = Window()
    print(getTask())
    for _ in range(10):
        mywin = Window()
        mywin._setImg(rootImg)
        mywin._locate(randomEdge(mywin.root))
        
    main.root.mainloop()
    
# _test()