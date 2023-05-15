import occur,draw,fun
import ame,gen,window,getweb

# sound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

setting = ame.Config(
    frameRate = 60,
    speedPerSec = 600
)

ameImg = getweb.AmeImg()

def main(self):
    
    # stand, and basic pose
    def _stand(end):
        if(fun.percent(7)):
            # eat cake
            self.poseManager.setPose(draw.PoseList.eat,draw.MorePose(1,end))
        else:
            # stand
            self.poseManager.setPose(draw.PoseList.stand,draw.MorePose(1,end))
    
     # main
    def _run(end):
        # run
        self.moveManager.moveToward(None,end)
        self.poseManager.setPose(draw.PoseList.walk)
        
        def backNormal():
            self.poseManager.setPose(draw.PoseList.walk)
            
        def runPoseSelc():
            if(fun.percent(50,setting.frameRate)):
                self.poseManager.setPose(draw.PoseList.roll,draw.MorePose(1,backNormal))

        return runPoseSelc
    
    def _windowPicker(end):
        
        def _endThings():
            self.moveManager.detach(mywin)
            end()
        
        def _pullWindow():
            # pull window
            self.moveManager.attach(mywin,edgeAdder)
            print(edgeAdder)
            self.moveManager.moveToward(pos,_endThings)
        
        # get now pos
        pos = self.moveManager.nowPos
        edgeAdder = (0,0)
        
        # get some random window
        mywin = window.Window()
        mywin._setImg(ameImg.get())
        mywin._locate(window.randomEdge(mywin.root))
        self.root.lift()
        
        # get edge of the window
        edgeAdder = mywin._getEdge()
        
        # move to random window
        self.poseManager.setPose(draw.PoseList.walk)
        self.moveManager.moveToward(fun.addVector(mywin.pos,fun.reVector(edgeAdder)),_pullWindow)
    
    # onclick  
    def _onclick(end):
        # groundpound
        self.poseManager.setPose(draw.PoseList.jump,draw.MorePose(1,end))
        ame.Run(main,setting,False,self.moveManager.nowPos)
        
        
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
        # muse
        self.poseManager.setPose(draw.PoseList.muse,draw.MorePose(10,end))
        
    cmds = [
        occur.Command(occur.When(setting.frameRate,percent=setting.ALWAYS),_stand,5),
        occur.Command(occur.When(setting.frameRate,percent=70),_run,4),
        occur.Command(occur.When(clicked=0),_onclick,3),
        occur.Command(occur.When(checker=_museChecker),_museOn,2),
        occur.Command(occur.When(setting.frameRate,percent=1/60 * 100),_windowPicker,1),
    ]
    return cmds
    

gen.Gen(main,setting)