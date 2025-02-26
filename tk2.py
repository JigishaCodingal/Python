from tkinter import *
from PIL import Image, ImageTk
T=Tk()
T.title('Image Window')
T.geometry('400x400')
Img=Image.open('i6.jpeg')
Img=ImageTk.PhotoImage(Img)
L1=Label(T,image=Img,height=300,width=300)
L1.place(x=50,y=0)
L2=Label(T,text="This is how you add an image in Tkinter window")
L2.place(x=40,y=300)
T.mainloop()