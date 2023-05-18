import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="timer = 0")
label.pack()
nowTime=0

def nextTime():
    global root,label,nowTime
    label.config(text=nowTime)
    
    nowTime+=1
    root.after(1000, nextTime)
    
nextTime()

# child window
root.after(0,tk.Toplevel)

tk.mainloop()