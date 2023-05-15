import random

# percentage to run 0~100
def percent(percentage, frameRate=1):
    if(random.uniform(0,100) <= percentage/frameRate):
        return True
    else:
        return False
    
def _test(percentage,frameRate=1,time = 1):
    sumNum = 0
    repTime = time * frameRate
    for _ in range(repTime):
        if(percent(percentage,frameRate)):
            sumNum+=1
            
    print(f"average percent to run for one execute {sumNum/(repTime) * 100 * frameRate}%")
    print(f"total {sumNum} times executed for time {time}s")
    
# _test(0.5,frameRate=60,time = 3600)