import math
import random
import window

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
        self.ceased = True
        
        # locate randomly
        if(pos == None):
            self._locate(window.randomPos(self.root))
        else:
            self._locate(pos)
            
        # target pos
        self._setPoint()
    
    def _locate(self, targetPos):
        self.root.geometry(f'+{int(targetPos[0])}+{int(targetPos[1])}')
        self.nowPos = targetPos
        
    def _moveDir(self,targetDir):
        rx,ry = self.nowPos
        dx,dy = targetDir
        
        self._locate((rx+dx,ry+dy))
    
    def _getWindowSize(self):
        return self.root.winfo_width(), self.root.winfo_height()
    
    def _reached(self):
        self.targetDir = (0,0)
        self._locate(self.targetPos)
        self.timer = 0
        
        self._setPoint()
        
    def _setPoint(self,pos=None):
        if pos == None:
            pos = window.randomPos(self.root)
            
        self.targetPos = pos
        self.timer = 0
        
        #calculate estimate time
        distance = math.dist(self.nowPos,self.targetPos)
        self.estimateTime = int(distance / self.speedPerFrame)
        normed = _norm(self.nowPos,self.targetPos)
        self.targetDir = (normed[0]*self.speedPerFrame, normed[1]*self.speedPerFrame)
        
    def start(self):
        self.ceased = False
        
    def end(self):
        self.ceased = True
    
    def nextFrame(self):
        if(not self.ceased):
            if(self.estimateTime <= self.timer):
                self._reached()

            self._moveDir(self.targetDir)
            self.timer += 1

def getWait():
    return random.randrange(3000,8000)
    
def _norm(startPos,endPos):
    sx,sy = startPos
    ex,ey = endPos
    
    x,y = ex-sx , ey-sy
    
    dist = math.dist((0,0),(x,y))
    
    return (x/dist,y/dist)