import window,fun

class AttachedWindow:
    def __init__(self,winRoot:window.Window,to):
        self.winRoot = winRoot
        self.to = to
        
        # calc offset
        self.offset = fun.addVector(winRoot.pos , fun.reVector(to.moveManager.nowPos))

class AttachManager:
    def __init__(self):
        self.attachList = []
        
    def attach(self,target):
        target.winRoot.root.attributes('-disabled', True)
        self.attachList.append(target)
        
        def detach():
            target.winRoot.root.attributes('-disabled', False)
            self.attachList.remove(target)
            
        return detach
        
    def nextFrame(self):
        for nowAttach in self.attachList:
            nowAttach.winRoot._locate(fun.addVector(nowAttach.to.moveManager.nowPos, nowAttach.offset))