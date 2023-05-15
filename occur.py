import random

class When:
    def __init__(self,frameRate = -1,clicked=-1, percent=-1,checker=None):
        self.checker = checker
        self.clicked = clicked
        self.percent = percent/frameRate

class Command:
    def __init__(self, when, runner,runIndex):
        self.when = when
        self.runner=runner
        self.runIndex=runIndex
        
    def run(self,endRun):
        return self.runner(endRun)

class EventListener:
    def __init__(self, imgLabel,frameRate):
        
        # setting
        self.imgLabel = imgLabel
        self.event = [False,False,False]
        self._setEvent()
        self.randomValue = 100
        
        # for time calc
        self.frameRate = frameRate
        self.timer = 0
        
    def _clickOccur(self,num):
        def eventSetter(_):
            self.event[num] = True
           
        return eventSetter 
        
    def _setEvent(self):
        self.imgLabel.bind("<Button-1>",self._clickOccur(0))
        self.imgLabel.bind("<Button-2>",self._clickOccur(1))
        self.imgLabel.bind("<Button-3>",self._clickOccur(2))
        
    def resetEvent(self):
        self.event = [False,False,False]
        
    def makeRandom(self):
        self.randomValue = random.uniform(0,100)
        
    def calculateRun(self,when):
        
        if(when.checker != None):
            return when.checker()
        
        if(when.clicked != -1):
            return self.event[when.clicked]
        
        if(when.percent != -1):
            return when.percent>=self.randomValue
        
        

class OccurManager:
    def __init__(self,frameRate,imgLabel):
        self.commandList=[]
        self.availMethods=[]
        self.runIndex = -1
        self.imgLabel = imgLabel
        self.frameRate = frameRate
        self.startIndex = -1
        self.runCmdMethod = None
        
        # event listener
        self.eventListener = EventListener(self.imgLabel,frameRate)
        
    def occurList(self,cmds):
        self.commandList = (cmds)
        
    def calcRunIndex(self,runIndex):
        return self.runIndex == -1 or runIndex <= self.runIndex
        
    def endRun(self):
        self.runIndex = -1
        self.runCmdMethod = None
        
    def start(self,cmd):
        self.runIndex = cmd.runIndex-1
        self.runCmdMethod = cmd.run(self.endRun)
        
    def runCommands(self):
        for cmd in self.commandList:
            if self.calcRunIndex(cmd.runIndex) and self.eventListener.calculateRun(cmd.when):
                self.start(cmd)
        
    def nextFrame(self):
        
        self.eventListener.makeRandom()
        self.runCommands()
        if(self.runCmdMethod != None):
            self.runCmdMethod()
        self.eventListener.resetEvent()