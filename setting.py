class Config:
    def __init__(self,frameRate,speedPerSec):
        self.frameRate = frameRate
        self.speedPerSec = speedPerSec
        self.ALWAYS = 100 * frameRate
        
        self.screenSize = (-1,-1)
        self.appSize = (100,100)
        
        self.disruptRate = (1/120)* 100
        self.runRate = 70
        
main = None