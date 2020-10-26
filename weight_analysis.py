from tkinter import *
from PIL import ImageTk, Image
w1 = Tk()
w1.title("Weight Analysis")
h = Scrollbar(w1, orient='horizontal')
h.pack(side=BOTTOM, fill=X)
# create a vertical scrollbar-no need to write orient as it is by  default vertical
v = Scrollbar(w1)
v.pack(side=RIGHT, fill=Y)
load = ImageTk.PhotoImage(Image.open(
    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\WA#.jpg'))

l1=Label(w1,image=load)
l1.pack()
mainloop()
