import random
import setting

class When:
    def __init__(self,clicked=-1, percent=-1,checker=None):
        self.checker = checker
        self.clicked = clicked
        
        if(percent != -1):
            self.percent = percent/setting.main.frameRate
        else:
            self.percent = -1

class Command:
    def __init__(self, when, runner,runIndex):
        self.when = when
        self.runner=runner
        self.runIndex=runIndex
        
    def run(self,endRun):
        return self.runner(endRun)

class EventListener:
    def __init__(self):
        
        # setting
        self.randomValue = 100
        
        # for time calc
        self.timer = 0
        
        # click events
        self.clicked = [False,False]
        
    def makeRandom(self):
        self.randomValue = random.uniform(0,100)
        
    def setDefault(self):
        self.clicked= [False,False]
        
    def calculateRun(self,when):
        if(when.checker != None):
            return when.checker()
        
        if(when.percent != -1):
            return when.percent>=self.randomValue
        
        if(when.clicked != -1):
            return self.clicked[when.clicked]
        
        

class OccurManager:
    def __init__(self,getCmds):
        self.commandList=getCmds
        self.runIndex = -1
        self.frameRate = setting.main.frameRate
        self.startIndex = -1
        self.runCmdMethod = None
        self.eventListener = EventListener()
        
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
            
        self.eventListener.setDefault()