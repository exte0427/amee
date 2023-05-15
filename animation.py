import win32api
import random
import tkinter as tk

class AnimationManager:
    def __init__(self):
        self.aniThings = []
        self.delThings = []
        
    def add(self,aniThing):
        self.aniThings.append(aniThing)
        
    def _delete(self,aniThing):
        def _delnow():
            self.delThings.append(aniThing)
            
        return _delnow
        
    def nextFrame(self):
        self.delThings = []
        
        for aniThing in self.aniThings:
            aniThing(self._delete(aniThing))
            
        for aniThing in self.delThings:
            self.aniThings.remove(aniThing)
            
class Timer:
    def __init__(self,target):
        self.target = target
        self.time = 0
        
    def nextFrame(self):
        self.time += 1
        
    def isEnd(self):
        return self.time >= self.target
    
    def getNorm(self):
        return self.time/self.target
            
def genShake(time,intense,frameRate):
    myTimer = Timer(time*frameRate)
    def shake(end):
        if(myTimer.isEnd()):
            end()
            
        # calcuate intense
        realIntense = intense+ (1-(myTimer.getNorm()-0.5)) * intense
            
        # shake mouse
        x, y = win32api.GetCursorPos()
        offset_x = random.randint(-intense, intense)
        offset_y = random.randint(-intense, intense)
        win32api.SetCursorPos((x + offset_x, y + offset_y))
            
        myTimer.nextFrame()
        
    return shake

def _test():
    
    # first setting
    main = tk.Tk()
    animanager=AnimationManager()
    def frame():
        animanager.nextFrame()
        main.after(int(1000/60),frame)
    frame()
    
    animanager.add(genShake(2,10,60))
    
    main.mainloop()
    
# _test()