import math
import window,fun,setting

class MoveManager:
    def __init__(self,pos=None):
        self.frameRate = setting.main.frameRate
        self.speedPerFrame = setting.main.speedPerSec/self.frameRate
        
        self.targetDir = (0,0)
        self.targetPos = (0,0)
        self.nowPos = (0,0)
        self.attachWindow = []
        
        # internal
        self.estimateTime = 0
        self.timer = 0
        self.callback = None
        self.ceased = True
        
        # locate randomly
        if(pos == None):
            self._locate(window.randomPos())
        else:
            self._locate(pos)
    
    def _locate(self, targetPos):
        
        for nowWin in self.attachWindow:
            nowWin._locate(self.nowPos)
        
        self.nowPos = targetPos
        
    def _moveDir(self,targetDir):
        self._locate(fun.addVector(self.nowPos,targetDir))
    
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
            pos = window.randomPos()
            
        self.targetPos = pos
        self.timer = 0
        
        #calculate estimate time
        distance = math.dist(self.nowPos,self.targetPos)
        self.estimateTime = int(distance / self.speedPerFrame)
        normed = _norm(self.nowPos,self.targetPos)
        self.targetDir = (normed[0]*self.speedPerFrame, normed[1]*self.speedPerFrame)
        
    def moveToward(self,pos,callback=None):
        self.ceased = False
        self._setPoint(pos)
        self.callback=callback
        
    def attach(self,winRoot):
        self.attachWindow.append(winRoot)
        
    def detach(self,winRoot):
        self.attachWindow.remove(winRoot)
            
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
    
    if(dist != 0):
        return (x/dist,y/dist)
    else:
        return (0,0)