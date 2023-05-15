import math
import random
import window,fun

class MoveManager:
    def __init__(self,root,frameRate,speedPerSec,pos=None):
        self.root = root
        self.windowSize = (0,0)
        self.frameRate = frameRate
        self.speedPerFrame = speedPerSec/self.frameRate
        
        self.targetDir = (0,0)
        self.targetPos = (0,0)
        self.nowPos = (0,0)
        self.estimateTime = 0
        self.timer = 0
        self.callback = None
        self.ceased = True
        self.attachWindows = []
        self.attachConfig = []
        
        # locate randomly
        if(pos == None):
            self._locate(window.randomPos(self.root))
        else:
            self._locate(pos)
    
    def _locate(self, targetPos):
        
        for i,el in enumerate(self.attachWindows):
            el._locate(fun.addVector(targetPos,self.attachConfig[i]))
        
        self.root.geometry(f'+{int(targetPos[0])}+{int(targetPos[1])}')
        self.nowPos = targetPos
        
    def _moveDir(self,targetDir):
        self._locate(fun.addVector(self.nowPos,targetDir))

    def _getWindowSize(self):
        return self.root.winfo_width(), self.root.winfo_height()
    
    def _reached(self):
        self.targetDir = (0,0)
        self._locate(self.targetPos)
        self.timer = 0
        self.ceased = True

        if(self.callback != None):
            lastFunc = self.callback
            self.callback()
            if(lastFunc == self.callback):
                self.callback = None
        
    def _setPoint(self,pos=None):
        
        # if none, get random pos
        if pos == None:
            pos = window.randomPos(self.root)
            
        self.targetPos = pos
        self.timer = 0
        
        #calculate estimate time
        distance = math.dist(self.nowPos,self.targetPos)
        self.estimateTime = int(distance / self.speedPerFrame)
        normed = _norm(self.nowPos,self.targetPos)
        self.targetDir = (normed[0]*self.speedPerFrame, normed[1]*self.speedPerFrame)
        
    def moveToward(self,pos,callback):
        self.ceased = False
        self._setPoint(pos)
        self.callback=callback
        
    def attach(self,attachWindow,config):
        self.attachWindows.append(attachWindow)
        self.attachConfig.append(config)
    
    def detach(self,detachWindow):
        del self.attachConfig[self.attachWindows.index(detachWindow)]
        self.attachWindows.remove(detachWindow)
        
            
    def nextFrame(self):
        if(not self.ceased):
            if(self.estimateTime <= self.timer):
                self._reached()

            self._moveDir(self.targetDir)
            self.timer += 1
    
def _norm(startPos,endPos):
    sx,sy = startPos
    ex,ey = endPos
    
    x,y = ex-sx , ey-sy
    
    dist = math.dist((0,0),(x,y))
    
    return (x/dist,y/dist)