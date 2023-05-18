import tkinter as tk

class DrawManager:
    def __init__(self,myapp):
        self.myapp = myapp
        self.imgs = []
        
        # init img
        for ame in self.myapp.ameList:
            nowEl = self._genImg(ame.poseManager.nowImg)
            self._clickEvent(nowEl,ame)
            self.imgs.append(nowEl)
            
    def _clickEvent(self,targetImg,target):
        def genClick(i):
            def click(event):
                target.occurManager.eventListener.clicked[i] = True
                
            return click
        
        self.myapp.canvas.tag_bind(targetImg,"<Button-1>",genClick(0))
        self.myapp.canvas.tag_bind(targetImg,"<Button-3>",genClick(1))
        
    def _genImg(self,targetImg):
        return self.myapp.canvas.create_image(0, 0,anchor=tk.NW, image=targetImg)
    
    def _setImg(self,img,targetImg):
        self.myapp.canvas.itemconfig(img,image=targetImg)
        
    def _moveImg(self,targetImg,targetPos):
        self.myapp.canvas.moveto(targetImg,*targetPos)
        
    def nextFrame(self):

        for i,ame in enumerate(self.myapp.ameList):
            nowCharacter = self.imgs[i]
            self._setImg(nowCharacter,ame.poseManager.nowImg)
            self._moveImg(nowCharacter,ame.moveManager.nowPos)