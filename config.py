import occur,pose,fun
import ame,gen,window,getweb,animation,setting,attach
import random

# sound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

setting.main = setting.Config(
    frameRate = 60,
    speedPerSec = 600
)

ameImg = getweb.AmeImg()

def main(self:ame.Ame):
    
    # basic movements
    def _move(pos,end):
        # run
        self.moveManager.moveToward(pos,end)
        self.poseManager.setPose(pose.PoseList.walk)
        
        def backNormal():
            self.poseManager.setPose(pose.PoseList.walk)
            
        def runPoseSelc():
            
            # calc flip
            if(self.moveManager.targetDir[0] > 0):
                self.poseManager.flip(False)
            else:
                self.poseManager.flip(True)
            
            if(fun.percent(50)):
                self.poseManager.setPose(pose.PoseList.roll,pose.MorePose(1,backNormal))

        return runPoseSelc
    
    # stand, and basic pose
    def _stand(end):
        
        # stand
        self.moveManager.moveToward(self.moveManager.nowPos)
        
        if(fun.percent(4,True)):
            # eat cake
            self.poseManager.setPose(pose.PoseList.eat,pose.MorePose(random.randint(2,5),end))
        else:
            # stand
            self.poseManager.setPose(pose.PoseList.stand,pose.MorePose(1,end))
    
     # main
    def _run(end):
        return _move(None,end)
    
    def _windowPicker(end):
        
        def _endThings(detacher):
            def _end():
                print("!")
                detacher()
                end()
                
            return _end
        
        def _pullWindow():
            # pull window
            detacher = self.attachManager.attach(attach.AttachedWindow(mywin,to=self))
            self.moveManager.moveToward(pos,_endThings(detacher))
        
        # get now pos
        pos = self.moveManager.nowPos
        edgeAdder = (0,0)
        
        # get some random window
        mywin = window.Window()
        mywin._setImg(ameImg.get())
        mywin._locate(window.randomEdge(mywin.size))
        
        # get edge of the window
        edgeAdder = mywin._getEdge()
        
        # move to random window
        return _move(fun.addVector(mywin.pos,fun.reVector(edgeAdder)),_pullWindow)
    
    # gp
    def _groundpound(end):
        self.moveManager.moveToward(self.moveManager.nowPos)
        self.animationManager.add(animation.genShake(2.5,10))
        self.poseManager.setPose(pose.PoseList.jump,pose.MorePose(random.randint(8,10),end))
        
    # onclick
    def _onclick(end):
        end()
        
    # muse set
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    global lastvolume
    lastvolume = volume.GetMasterVolumeLevelScalar()
    
    def _museChecker():
        global lastvolume
        if(volume.GetMasterVolumeLevelScalar() != lastvolume):
            lastvolume = volume.GetMasterVolumeLevelScalar()
            return True
        else:
            return False
        
    def _museOn(end):
        
        # stand
        self.moveManager.moveToward(self.moveManager.nowPos)
        
        # muse
        self.poseManager.setPose(pose.PoseList.muse,pose.MorePose(10,end))
        
    def _disrupt(end):
        if(fun.percent(50,True)):
            return _windowPicker(end)
        else:
            return _groundpound(end)
        
    print(setting.main.disruptRate,setting.main.runRate)
    cmds = [
        occur.Command(occur.When(percent=setting.main.ALWAYS),_stand,6),
        occur.Command(occur.When(percent=setting.main.runRate),_run,5),
        occur.Command(occur.When(clicked=0),_onclick,4),
        occur.Command(occur.When(checker=_museChecker),_museOn,3),
        occur.Command(occur.When(percent=setting.main.disruptRate),_disrupt,2),
        # occur.Command(occur.When(percent=setting.main.ALWAYS),_windowPicker,1),
    ]
    return cmds
    

gen.Gen(main, dev=False)