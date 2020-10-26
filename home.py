from tkinter import *
import time
from PIL import ImageTk, Image


# def wa():
#   exec(open(r'C:\Users\HPSEDC\Desktop\project\weight_analysis.py').read())

class abc:

    def __init__(self):
        self.home = Tk()

        self.home.title("Home-Health Tracker and Recommender System")
        self.home.geometry('1728x1080')
        self.h = Scrollbar(self.home, orient='horizontal')
        self.h.pack(side=BOTTOM, fill=X)

        # create a vertical scrollbar-no need to write orient as it is by  default vertical
        self.img1 = ImageTk.PhotoImage(Image.open(
            r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\77Yc.jpg'))
        self.load = ImageTk.PhotoImage(Image.open(
            r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\bc.jpg'))

        self.v = Scrollbar(self.home)
        self.v.pack(side=RIGHT, fill=Y)
        self.label = Label(self.home, text="", width=14, height=3, bg="red",
                           fg="black", font=("chiller", 19, "bold"))
        self.label.pack(anchor='sw')
        self.label.after(100, self.clock)
        self.label2 = Label(self.home, bg="black", width=20, height=50)
        self.label2.pack(anchor='nw')
        self.b = Button(self.label2, image=self.img1, command=self.wa)
        self.b.pack()
        self.m = Message(self.label2, text="Weight Analysis", font=(
            "chiller", 16, "bold"), width=120, bg="light blue")

        self.m.pack()

        self.home.mainloop()

    def clock(self):
        self.hour = time.strftime("%I")
        self.minute = time.strftime("%M")
        self.second = time.strftime("%S")
        self.am_pm = time.strftime("%p")
        self.label.config(text=self.hour + ":" + self.minute +
                               ":" + self.second + self.am_pm)
        self.label.after(1000, self.clock)

    def wa(self):
        self.w1 = Tk()
        self.w1.title("Weight Analysis")
        self.h = Scrollbar(self.w1, orient='horizontal')
        self.h.pack(side=BOTTOM, fill=X)
        # create a vertical scrollbar-no need to write orient as it is by  default vertical
        self.v = Scrollbar(self.w1)
        self.v.pack(side=RIGHT, fill=Y)

        self.l1 = Label(self.w1, image=self.load)
        self.l1.pack()
        mainloop()


obj = abc()


