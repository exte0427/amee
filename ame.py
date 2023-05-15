import draw,occur,move,animation
import tkinter as tk

class Config:
    def __init__(self,frameRate,speedPerSec):
        self.frameRate = frameRate
        self.speedPerSec = speedPerSec
        self.ALWAYS = 100 * frameRate

class Run:
    def __init__(self, getCmds,config,pos=None):
        # gen
        self.root = tk.Toplevel()
        
        # borderless
        self.root.wm_attributes("-topmost", True)
        self.root.overrideredirect(True)
        
        # config get
        self.config = config
        self.pos = pos
        
        # run commands
        self.cmds = getCmds(self)

        # run
        self._start(self.root)

        # transparent
        self.root.config(bg = '#000001')
        self.root.wm_attributes('-transparentcolor','#000001')
        
    def _start(self,root):
        # set data
        self.commands=[]
        self.root = root
        
        # set managers
        self.moveManager = move.MoveManager(self.root,self.config.frameRate,self.config.speedPerSec,self.pos)
        self.poseManager = draw.PoseManager(self.root)
        self.occurManager = occur.OccurManager(self.config.frameRate,self.root)
        self.animationManager = animation.AnimationManager()
        
        # set initial values
        # self.poseManager.setPose(draw.PoseList.walk,self.root)
        
        # event setting
        self.occurManager.occurList(self.cmds)
        
        # run
        self._genFrame()
        

    def _genFrame(self):

        # manager
        self.poseManager.nextFrame()
        self.occurManager.nextFrame()
        self.moveManager.nextFrame()
        self.animationManager.nextFrame()
        
        # flip
        if(self.moveManager.targetDir[0] < 0):
            self.poseManager.flip(True)
        else:
            self.poseManager.flip(False)
        
        # end
        self.root.after(int(1000/self.config.frameRate),self._genFrame)
