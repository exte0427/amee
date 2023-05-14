import draw
import occur
import move
import tkinter as tk

class Config:
    def __init__(self,frameRate,speedPerSec):
        self.frameRate = frameRate
        self.speedPerSec = speedPerSec

class Run:
    def __init__(self, getCmds,config):
        # borderless
        self.root = tk.Tk()
        self.root.wm_attributes("-topmost", True)
        self.root.overrideredirect(True)
        
        # config get
        self.config = config
        
        # run commands
        self.cmds = getCmds(self)

        # run
        self._start(self.root)

        # transparent
        self.root.config(bg = '#add123')
        self.root.wm_attributes('-transparentcolor','#add123')
        
        self.root.mainloop()
        
    def _start(self,root):
        # set data
        self.commands=[]
        self.root = root
        
        # set managers
        self.poseManager = draw.PoseManager(self.root)
        self.occurManager = occur.OccurManager(self.config.frameRate,self.root)
        self.moveManager = move.MoveManager(self.root,self.config.frameRate,self.config.speedPerSec)
        
        # set initial values
        # self.poseManager.setPose(draw.PoseList.walk,self.root)
        
        # event setting
        self.occurManager.occurList(self.cmds)
        
        # base setting
        self.occurManager.onStart(0);
        
        # run
        self._genFrame()
        

    def _genFrame(self):
        # start code
        
        # manager
        self.poseManager.nextFrame()
        self.occurManager.nextFrame()
        self.moveManager.nextFrame()
        
        # flip
        if(self.moveManager.targetDir[0] < 0):
            self.poseManager.flip(True)
        else:
            self.poseManager.flip(False)
        
        # end
        self.root.after(int(1000/self.config.frameRate),self._genFrame)
