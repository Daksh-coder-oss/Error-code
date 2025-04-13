from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert!Error Code!")
button=Button(root,text="If clicked There will be an error code",command=msg)
button.place(x=40,y=50)
root.mainloop()