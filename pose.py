from enum import Enum
from PIL import Image,ImageTk,ImageSequence
class PoseList(Enum):
    stand=0
    walk =1
    jump = 2
    eat=3
    muse = 4
    roll = 5
    none=6
    
class GIFGetter:
    def __init__(self):
        self.gif = {
            "walk":extractGif("ame/walk.gif"),
            "stand":extractGif("ame/stand.gif"),
            "jump":extractGif("ame/jump.gif"),
            "eat":extractGif("ame/eat.gif"),
            "muse":extractGif("ame/muse.gif"),
            "roll":extractGif("ame/roll.gif")
        }
        
    def getFile(self,pose):
        return self.gif[pose.name]
        
class MorePose:
    def __init__(self,repeatNum, endfunc):
        self.repeatNum = repeatNum
        self.endfunc = endfunc
        self.nowCount = 0
        
    def calcCount(self):
        
        self.nowCount+=1
        
        if(self.repeatNum <= self.nowCount):
            self.endfunc()
        
        
class PoseManager:
    def __init__(self):
        
        # set pictures
        self.picList =[]
        self.nowPos = PoseList.none
        self.nowFrame = 0
        self.isFlip = False
        self.morePose = None
        
        # output data
        self.nowImg = None
        
        # set GIFGetter
        self.gifGetter=GIFGetter()
        
        # first size
        self._setGif(self.gifGetter.getFile(PoseList.stand))
        
    def _setGif(self,gifList):
        self.picList = gifList
        self.isFlip = False
        
        self.nowFrame = 0 

    def setPose(self,newPose, morePose=None):
        if(self.nowPos != newPose):
            self._setGif(self.gifGetter.getFile(newPose))
            
            self.nowPos = newPose
            self.morePose = morePose
            
    def flip(self,isFlip):
        if((not self.isFlip and isFlip) or (self.isFlip and not isFlip)):
            flipedList = []
            for pic in self.picList:
                flipedList.append(pic.transpose(Image.FLIP_LEFT_RIGHT))
                
            self.picList = flipedList
            self.isFlip = isFlip
        
    def _getNow(self):
        nowFrame = ImageTk.PhotoImage(self.picList[self.nowFrame])
        return nowFrame 
        
    def nextFrame(self):
        self.nowImg = self._getNow()
        
        if(self.nowFrame+1 < len(self.picList)):
            self.nowFrame += 1
        else:
            if(self.morePose != None):
                self.morePose.calcCount()
            
            self.nowFrame = 0

def extractGif(path):
    img = Image.open(path)
    frames = []
    for frame in ImageSequence.Iterator(img):
        frames.append(frame.copy())
        
    return frames