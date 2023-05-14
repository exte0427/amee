import win32api,win32con
import time
import random

def shake(durTime,magni,frame=60):
    for i in range(int(durTime*frame)):
        randomRange = (durTime*frame - i) * magni
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, random.randrange(-randomRange,randomRange), random.randrange(-randomRange,randomRange), 0, 0)
        time.sleep(1/frame)
        
shake(0.3,1)