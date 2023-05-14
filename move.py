import math
import random
import window

class MoveManager:
    def __init__(self,root,frameRate,speedPerSec):
        self.root = root
        self.windowSize = (0,0)
        self.frameRate = frameRate
        self.speedPerFrame = speedPerSec/self.frameRate
        
        self.targetDir = (0,0)
        self.targetPos = (0,0)
        self.estimateTime = 0
        self.timer = 0
        self.ceased = True
        
        self._setPoint()
        
        # locate randomly
        _locate(self.root,window.randomPos(self.root))
        
    def _getWindowSize(self):
        return self.root.winfo_width(), self.root.winfo_height()
    
    def _reached(self):
        self.targetDir = (0,0)
        _locate(self.root,self.targetPos)
        self.timer = 0
        
        self._setPoint()
        
    def _setPoint(self,pos=None):
        if pos == None:
            pos = window.randomPos(self.root)
            
        self.targetPos = pos
        self.timer = 0
        
        #calculate estimate time
        distance = math.dist(_getPos(self.root),self.targetPos)
        self.estimateTime = int((distance / self.speedPerFrame))
        normed = _norm(_getPos(self.root),self.targetPos)
        self.targetDir = (normed[0]*self.speedPerFrame, normed[1]*self.speedPerFrame)
        
    def start(self):
        self.ceased = False
        
    def end(self):
        self.ceased = True
    
    def nextFrame(self):
        if(not self.ceased):
            if(self.estimateTime <= self.timer):
                self._reached()

            _moveDir(self.root,self.targetDir)
            self.timer += 1

def getWait():
    return random.randrange(3000,8000)

def _locate(root, targetPos):
    root.geometry(f'+{int(targetPos[0])}+{int(targetPos[1])}')
    
def _getPos(root):
        return root.winfo_x(), root.winfo_y()
    
def _moveDir(root,targetDir):
    rx,ry = _getPos(root)
    dx,dy = targetDir
    
    _locate(root,(rx+dx,ry+dy))
    
def _norm(startPos,endPos):
    sx,sy = startPos
    ex,ey = endPos
    
    x,y = ex-sx , ey-sy
    
    dist = math.dist((0,0),(x,y))
    
    return (x/dist,y/dist)