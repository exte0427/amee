import occur,move,pose,attach,animation

class Ame:
    def __init__(self,getCmds):
        self.moveManager:move.MoveManager = move.MoveManager()
        self.occurManager:occur.OccurManager = occur.OccurManager(getCmds(self))
        self.poseManager:pose.PoseManager = pose.PoseManager()
        self.attachManager:attach.AttachManager = attach.AttachManager()
        self.animationManager:animation.AnimationManager = animation.AnimationManager()
        
    def nextFrame(self):
        self.moveManager.nextFrame()
        self.occurManager.nextFrame()
        self.poseManager.nextFrame()
        self.attachManager.nextFrame()
        self.animationManager.nextFrame()