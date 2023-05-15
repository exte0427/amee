import occur,draw,fun
import ame,gen

# sound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

setting = ame.Config(
    frameRate = 60,
    speedPerSec = 600
)

def main(self):
    
     # main
    def _mainEvent(end):
        if(fun.percent(40)):
            # run
            self.moveManager.start()
            self.poseManager.setPose(draw.PoseList.walk)
            
            def backNormal():
                self.poseManager.setPose(draw.PoseList.walk)

            def runPoseSelc():
                if(fun.percent(50,setting.frameRate)):
                    self.poseManager.setPose(draw.PoseList.roll,draw.MorePose(1,backNormal))

            return runPoseSelc
        
        else:
            if(fun.percent(75)):
                # stand
                self.moveManager.end()
                self.poseManager.setPose(draw.PoseList.stand)
            else:
                # eat cake
                self.moveManager.end()
                self.poseManager.setPose(draw.PoseList.eat)
    
    # onclick  
    def _onclick(end):
        # groundpound
        self.moveManager.end()
        self.poseManager.setPose(draw.PoseList.jump,draw.MorePose(1,end))
        ame.Run(main,setting,False,self.moveManager.nowPos)
        
        
    # muse
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
        # muse
        self.moveManager.end()
        self.poseManager.setPose(draw.PoseList.muse,draw.MorePose(10,end))
        
    cmds = [
        occur.Command(occur.When(setting.frameRate,percent=50),_mainEvent,2),
        occur.Command(occur.When(clicked=0),_onclick,1),
        occur.Command(occur.When(checker=_museChecker),_museOn,0)
    ]
    return cmds
    

gen.Gen(main,setting)