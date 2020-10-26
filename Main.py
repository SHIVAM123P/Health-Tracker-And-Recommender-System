from tkinter import *
from PIL import ImageTk, Image
import time
import webbrowser
import math


class main1:
    # main inter face
    def __init__(self):
        self.win = Tk()
        self.win.geometry('1728x1080')
        self.f1 = PanedWindow()
        self.f1.pack(side='bottom')

        self.win.title('Health Tracker and Recommender System')
        self.load = Image.open(r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\77Yc.jpg')
        self.render = ImageTk.PhotoImage(self.load)
        self.login = Image.open(r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\multic.jpg')
        self.rendr = ImageTk.PhotoImage(self.login)
        self.images = Image.open(
            r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\multi2s.jpg')
        self.sign = ImageTk.PhotoImage(self.images)
        self.img = Label(self.win, image=self.render)
        self.img.place(x=0, y=15)
        self.s = Label(self.win, text='Health Tracker and Recommender System',
                       width=1500, borderwidth=3, relief='sunken', fg='orange')
        self.photo = ImageTk.PhotoImage(file=r"C:\Users\shivam kumar\Downloads\project_zipFinal\project\fbc.jpg")
        # photoimage = photo.ImageTK.subsample(3, 3)
        self.s.config(font=('algerian', 36, 'italic bold'))
        self.s.pack(fill='x')

        self.s.after(5000, self.update)

        self.b1 = Button(self.win, image=self.rendr, command=self.login1)
        self.b1["bg"] = "blue"
        self.b1["border"] = "10"
        self.b1.pack(pady=20)
        self.m1 = Message(self.win, text='if dont have an Account?', width=800)
        self.m1.config(font=('chiller', 18, 'bold'), bg='blue', fg='red')
        self.m1.pack(pady=20)
        self.b3 = Button(self.win, image=self.sign, command=self.signup)
        self.b3["bg"] = "blue"
        self.b3["border"] = "10"
        self.b3.pack()
        self.m3 = Message(self.win, text='OR')
        self.m3.config(font=('chiller', 18, 'bold'), bg='orange', fg='yellow')
        self.m3.pack(pady=20)
        self.b3 = Button(self.win, image=self.photo, command=self.home)

        self.b3.pack()
        self.win.mainloop()

    def login1(self):  # fun for logong in to the gui
        self.load1 = Image.open(r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\submit1.jpg')
        self.render1 = ImageTk.PhotoImage(self.load1)
        self.top = PanedWindow()
        self.top.pack(padx=20)
        self.m = Label(self.top, text='Username:', font=(
            'callibri', 10, 'bold'), bg='orange')
        self.top.add(self.m)
        self.top1 = PanedWindow(self.top)
        self.top1.pack()
        self.e = Entry(self.top1)
        self.e.pack()
        self.top.add(self.top1)
        self.top2 = PanedWindow()
        self.top2.pack()
        self.m1 = Label(self.top2, text='Password:', font=(
            'callibri', 10, 'bold'), bg='orange')
        self.top2.add(self.m1)
        self.top3 = PanedWindow(self.top2)
        self.e1 = Entry(self.top3)
        self.e1.pack()
        self.top2.add(self.top3)
        self.b = Button(self.win, image=self.render1, command=self.home)
        self.b.pack()
        mainloop()

    def signup(self):  # fun for siging up to the gui
        self.load1 = Image.open(r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\submit1.jpg')
        self.render1 = ImageTk.PhotoImage(self.load1)
        self.top = PanedWindow()
        self.top.pack(padx=20)
        self.m = Label(self.top, text='Username:', font=(
            'callibri', 10, 'bold'), bg='orange')
        self.top.add(self.m)
        self.top1 = PanedWindow(self.top)
        self.top1.pack()
        self.e = Entry(self.top1)
        self.e.pack()
        self.top.add(self.top1)
        self.top2 = PanedWindow()
        self.top2.pack()
        self.m1 = Label(self.top2, text='Password:', font=(
            'callibri', 10, 'bold'), bg='orange')
        self.top2.add(self.m1)
        self.top3 = PanedWindow(self.top2)
        self.e1 = Entry(self.top3)
        self.e1.pack()
        self.top2.add(self.top3)
        self.top4 = PanedWindow()
        self.top4.pack()
        self.m2 = Label(self.top4, text='Confirm Password:', font=(
            'callibri', 10, 'bold'), bg='orange')
        self.top4.add(self.m2)
        self.top5 = PanedWindow(self.top4)
        self.e2 = Entry(self.top5)
        self.e2.pack()
        self.top4.add(self.top5)
        self.b = Button(self.win, image=self.render1, command=self.home)
        self.b.pack()
        mainloop()

    def home(self):  # home window
        class abc:
            def __init__(self):

                self.home = Toplevel()
                self.img1 = Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\chubby11.jpg')
                self.load = ImageTk.PhotoImage(self.img1)
                self.bmi1 = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\bmi.png'))
                self.home.title("Home:-Health Tracker and Recommender System")
                self.bc1 = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\night.jpg'))
                self.ex = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\exerc.jpg'))
                self.dyt = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\diet.jpg'))
                self.dyt_plans = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\plans.png'))

                self.devlp = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\develpr.jpg'))
                self.bc2 = ImageTk.PhotoImage(Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\bc2.jpg'))
                self.home.geometry('1728x1080')
                self.health_calc = ImageTk.PhotoImage(Image.open(r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\health_cal.jpg'))
                self.f = Frame(self.home)  # right frame
                self.f.pack(side=RIGHT, anchor='ne')
                self.label1 = Label(self.f, image=self.bc1, width=15, height=3, bg="yellow",
                                    fg="blue", font=("chiller", 19, "bold"))
                self.label1.pack(anchor='sw')
                self.br1 = Button(self.label1, image=self.dyt, command=self.diet_plans_fun)
                self.br1["border"] = "10"
                self.br1["bg"] = "blue"
                self.br1.pack(padx=20, pady=(46, 0))
                self.dytm = Message(self.label1, text="Diet Recommendation", font=(
                    "chiller", 16, "bold"), width=120, bg="blue", fg="white")

                self.dytm.pack()
                self.br2 = Button(self.label1, image=self.health_calc, command=self.health_calculator)
                self.br2["border"] = "10"
                self.br2["bg"] = "blue"
                self.br2.pack(padx=20, pady=(50, 0))
                self.calm = Message(self.label1, text="Health Calculator", font=("chiller", 16, "bold"), width=120,
                                    bg="blue", fg="white")
                self.calm.pack()
                self.br3 = Button(self.label1, image=self.devlp, command=self.devlpr)
                self.br3["border"] = "10"
                self.br3["bg"] = "blue"
                self.br3.pack(padx=20, pady=(46, 0))
                self.dev = Message(self.label1, text="Developer Details", font=("chiller", 16, "bold"), width=120,
                                   bg="blue", fg="white")
                self.dev.pack()
                self.quit = Button(self.label1, text="Exit", font=('bold'), command=self.home.destroy)
                self.quit["border"] = "10"
                self.quit["bg"] = "blue"
                self.quit.pack(padx=20, pady=20)
                self.f1 = Frame(self.home, height=60)  # left frame
                self.f1.pack(side=LEFT, anchor='nw')
                self.label2 = Label(self.f1, image=self.bc1, height=60)
                self.label2.pack(anchor='nw')
                self.b = Button(self.label2, image=self.load, command=self.wa)
                self.b["border"] = "10"
                self.b["bg"] = "red"
                self.b.pack(padx=20)
                self.m = Message(self.label2, text="Weight Analysis", font=(
                    "chiller", 16, "bold"), width=120, bg="blue", fg="white")
                self.m.pack()
                self.b2 = Button(self.label2, image=self.bmi1,
                                 command=self.bmi2)
                self.b2["border"] = "10"
                self.b2.pack(pady=(20, 0), padx=20)
                self.m1 = Message(self.label2, text="Body Mass Index", font=(
                    "chiller", 16, "bold"), width=120, bg="blue", fg="white")
                self.m1.pack()
                self.b3 = Button(self.label2, image=self.ex,
                                 command=self.exer)
                self.b3["border"] = "10"
                self.b3["bg"] = "red"
                self.b3.pack(pady=(23, 0), padx=20)
                self.m2 = Message(self.label2, text="Exercise Videos", font=(
                    "chiller", 16, "bold"), width=120, bg="blue", fg="white")
                self.m2.pack()
                self.f2 = Frame(self.home, height=60)
                self.f2.pack(side=RIGHT)
                self.label = Label(self.f1, text="", width=15, height=3, bg="black",
                                   fg="blue", font=("chiller", 25, "bold"))
                self.label.pack(anchor='sw', side=BOTTOM)
                self.label.after(100, self.clock)
                self.f0 = Frame(self.home, height=1500, bg='black')

                self.centre = Label(self.f0, image=self.bc2, height=1000)
                self.centre.pack()
                self.f0.pack(side=LEFT, anchor='nw', fill=X)
                self.home.mainloop()

            def devlpr(self):
                self.details = Toplevel()
                self.details.title("Developer Details: -Health Tracker and Recommender System")
                self.leader = Label(self.details, text="Team Leader: Ashish Kumar Sharma | Regno.:11913573",
                                    font=('broadway', 30, 'bold'), fg='blue')
                self.leader.pack(pady=25)
                self.membr1 = Label(self.details, text="Team Member 1: Shivam Kumar Singh | Regno.:11913070", font=(
                    'broadway', 30), fg='red')
                self.membr1.pack(pady=25)
                self.membr2 = Label(self.details, text="Team Member 2: Muge Shubham  | Regno.:11910856", font=(
                    'broadway', 30), fg='green')
                self.membr2.pack(pady=(25, 0))

                self.membr3 = Label(self.details, text='Jalindarappa', font=(
                    'broadway', 30), fg='green')
                self.membr3.pack(pady=5)

            def bmi2(self):
                self.bdy = Toplevel()
                self.bdy.title("BMI: -Health Tracker and Recommender System")
                self.bdy.geometry('720x540')
                self.ent1 = IntVar()
                self.ent2 = IntVar()
                self.p = PanedWindow(self.bdy)
                self.p.pack()
                self.M = Label(self.p, text='Your Height(in meter)', font=(
                    'callibri', 10, 'bold'), bg='orange')
                self.p.add(self.M)
                self.p1 = PanedWindow(self.p)
                self.p1.pack()
                self.E = Entry(self.p1, textvariable=self.ent1)  # height entry
                self.E.pack()
                self.p.add(self.p1)

                self.p2 = PanedWindow(self.bdy)
                self.p2.pack()
                self.M1 = Label(self.p2, text='Your Weight(in kg)', font=(
                    'callibri', 10, 'bold'), bg='orange')
                self.p2.add(self.M1)
                self.p3 = PanedWindow(self.p2)
                self.E1 = Entry(self.p3, textvariable=self.ent2)  # mass entry
                self.E1.pack()
                self.p2.add(self.p3)
                self.but = Button(self.bdy, text="Submit", command=self.re)
                self.but.pack()

            def health_calculator(self):
                self.issues = Toplevel()
                self.sub = Image.open(
                    r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\submit1.jpg')
                self.sub1 = ImageTk.PhotoImage(self.sub)
                self.entry = StringVar()
                self.entry1 = IntVar()
                self.entry2 = IntVar()
                self.entry3 = IntVar()
                self.entry4 = IntVar()
                self.entry5 = IntVar()
                self.entry6 = IntVar()
                self.entry7 = IntVar()
                self.entry8 = IntVar()
                self.frame1 = Frame(self.issues)
                self.frame1.pack(side=LEFT, anchor='nw')
                self.inf1 = PanedWindow(self.frame1)
                self.inf1.pack()
                self.line1 = Label(self.inf1, text='Name:', font=(
                    'callibri', 10, 'bold'), bg='orange')
                self.line1.pack()
                self.inf1.add(self.line1)
                self.inf2 = PanedWindow(self.inf1)
                self.inf2.pack()
                self.entr = Entry(self.inf2, textvariable=self.entry)
                self.entr.pack()
                self.inf1.add(self.inf2)
                self.frame2 = Frame(self.issues)
                self.frame2.pack(side=TOP, anchor='nw')
                self.inf3 = PanedWindow(self.frame2)
                self.inf3.pack()
                self.line2 = Label(self.inf3, text="Age:", font=('callibri', 10, 'bold'), bg='orange')
                self.inf3.add(self.line2)
                self.inf4 = PanedWindow(self.inf3)
                self.entr1 = Entry(self.inf4, textvariable=self.entry1)
                self.entr1.pack()
                self.inf3.add(self.inf4)
                self.frame3 = Frame(self.frame1)
                self.frame3.pack(side=TOP, anchor='nw', pady=30)
                self.inf5 = PanedWindow(self.frame3)
                self.inf5.pack()
                self.line3 = Label(self.inf5, text='Gender:', font=(
                    'callibri', 10, 'bold'), bg='orange')
                self.inf5.add(self.line3)
                self.inf6 = PanedWindow(self.inf5)
                self.inf6.pack()
                self.inf5.add(self.inf6)
                self.entr2 = Radiobutton(
                    self.inf6, text='Male', variable=self.entry2, value=1)
                self.entr2.pack()

                self.inf6.add(self.entr2)
                self.inf7 = PanedWindow(self.inf6)
                self.inf7.pack()

                self.inf6.add(self.inf7)
                self.entr3 = Radiobutton(
                    self.inf7, text='Female', variable=self.entry2, value=2)
                self.entr3.pack()

                self.inf7.add(self.entr3)
                self.entry2.set(1)
                self.frame4 = Frame(self.frame1)
                self.frame4.pack(side=TOP, anchor='nw', pady=(30, 0))
                self.inf8 = PanedWindow(self.frame4)
                self.inf8.pack()
                self.bp_low = Label(self.inf8, text="BP Low", font=(
                    'callibri', 10, 'bold'), bg='orange')
                self.bp_low.pack()
                self.inf8.add(self.bp_low)
                self.entr4 = Entry(self.inf8, textvariable=self.entry4)
                self.entr4.pack()
                self.inf8.add(self.entr4)
                self.frame5 = Frame(self.frame1)
                self.frame5.pack(side=TOP, anchor='nw', )
                self.inf9 = PanedWindow(self.frame5)
                self.inf9.pack()
                self.bp_high = Label(self.inf9, text="BP High", font=('callibri', 10, 'bold'), bg='orange')
                self.bp_high.pack()
                self.inf9.add(self.bp_high)
                self.entr5 = Entry(self.inf9, textvariable=self.entry5)
                self.entr5.pack()
                self.inf9.add(self.entr5)
                self.frame6 = Frame(self.frame1)
                self.frame6.pack(side=TOP, anchor='nw', )
                self.inf10 = PanedWindow(self.frame6)
                self.inf10.pack()

                self.pulse = Label(self.inf10, text="Pulse rate", font=('callibri', 10, 'bold'), bg='orange')
                self.pulse.pack()
                self.inf10.add(self.pulse)
                self.entr6 = Entry(self.inf10, textvariable=self.entry6)
                self.entr6.pack()
                self.inf10.add(self.entr6)
                self.frame7 = Frame(self.frame1)
                self.frame7.pack(side=TOP, anchor='nw', )
                self.inf11 = PanedWindow(self.frame7)
                self.inf11.pack()
                self.haemoglobin = Label(self.inf11, text="Haemoglobin:", font=('callibri', 10, 'bold'), bg='orange')
                self.haemoglobin.pack()
                self.inf11.add(self.haemoglobin)
                self.entr7 = Entry(self.inf11, textvariable=self.entry7)
                self.entr7.pack()
                self.inf11.add(self.entr7)
                self.frame8 = Frame(self.frame1)
                self.frame8.pack(side=TOP, anchor='nw', )
                self.inf12 = PanedWindow(self.frame8)
                self.inf12.pack()
                self.cholestrol = Label(self.inf12, text="cholestrol", font=(
                    'callibri', 10, 'bold'), bg='orange')
                self.cholestrol.pack()
                self.inf12.add(self.cholestrol)
                self.entr8 = Entry(self.inf12, textvariable=self.entry8)
                self.entr8.pack()
                self.inf12.add(self.entr8)
                self.report = Button(self.frame8, image=self.sub1, command=self.report_fun)
                self.report.pack(padx=30, pady=25)
                mainloop()

            def report_fun(self):
                self.report1 = Toplevel()
                self.name_p = Label(self.report1, text="Name: " + str(self.entry.get()), font=('callibri', 15, 'bold'))
                self.name_p.pack(side=TOP, anchor='nw', pady=10)
                self.age_p = Label(self.report1, text="Age: " + str(self.entry1.get()), font=('callibri', 15, 'bold'))
                self.age_p.pack(side=TOP, anchor='nw', pady=10)
                if (int(self.entry2.get()) == 1):
                    self.ml = Label(self.report1, text="Gender: Male", font=('callibri', 15, 'bold'))
                    self.ml.pack(anchor='nw')
                else:
                    self.fl = Label(self.report1, text="Gender: Female", font=(
                        'callibri', 15, 'bold'))
                    self.fl.pack(anchor='nw')
                if (int(self.entry1.get()) <= 18):
                    self.bp_report()
                elif (int(self.entry1.get()) > 18 and int(self.entry1.get()) <= 40):
                    self.bp_report1()

                else:
                    self.bp_report2()

            def bp_report(self):
                if (int(self.entry4.get()) < 90):
                    self.bp_low_lab = Label(
                        self.report1, text="1).Your Bp Is low", font=('callibri', 10, 'bold'))
                    self.bp_low_lab.pack(side=TOP, anchor='nw', pady=10)
                elif (int(self.entry5.get()) > 120):
                    self.bp_high_lab = Label(
                        self.report1, text="1).Your bp Is high", font=('callibri', 10, 'bold'))
                    self.bp_high_lab.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.bp_nor = Label(self.report1, text="1).Your bp is normal", font=('callibri', 10, 'bold'))
                    self.bp_nor.pack(side=TOP, anchor='nw', pady=10)
                self.pulse_rt()

            def pulse_rt(self):

                if (int(self.entry6.get()) >= 70 and int(self.entry6.get()) <= 100):
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is normal", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)

                elif (int(self.entry6.get()) > 100):
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is quite high", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is quite low", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)
                self.haemoglobin_report()

            def haemoglobin_report(self):
                if (float(self.entry7.get()) >= 12.7 and float(self.entry7.get() <= 17.7)):
                    self.himo = Label(self.report1, text="3).Your haemoglobin level is good", font=(
                        'callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                elif (float(self.entry7.get()) > 17.7):
                    self.himo = Label(self.report1, text="3).Your haemoglobin level is quiet high",
                                      font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.himo = Label(self.report1, text="3).Your haemoglobin level is low",
                                      font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                self.cholestrol_report()

            def cholestrol_report(self):
                if (int(self.entry8.get()) >= 200 and int(self.entry8.get() <= 239)):
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol is in good level", font=('callibri', 10, 'bold'))
                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)
                elif (int(self.entry8.get()) > 240):
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol level is high", font=('callibri', 10, 'bold'))

                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol level is low", font=('callibri', 10, 'bold'))
                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)

            def bp_report1(self):
                if (int(self.entry4.get()) < 95):
                    self.bp_low_lab = Label(
                        self.report1, text="1).Your Bp Is low", font=('callibri', 10, 'bold'))
                    self.bp_low_lab.pack(side=TOP, anchor='nw', pady=10)
                elif (int(self.entry5.get()) > 135):
                    self.bp_high_lab = Label(
                        self.report1, text="1).Your bp Is high", font=('callibri', 10, 'bold'))
                    self.bp_high_lab.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.bp_nor = Label(self.report1, text="1).Your bp is normal", font=('callibri', 10, 'bold'))
                    self.bp_nor.pack(side=TOP, anchor='nw', pady=10)
                self.pulse_rt1()

            def pulse_rt1(self):

                if (int(self.entry6.get()) >= 60 and int(self.entry6.get()) <= 100):
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is normal", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)

                elif (int(self.entry6.get()) > 100):
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is quite high", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is quite low", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)
                self.haemoglobin_report1()

            def haemoglobin_report1(self):
                if (float(self.entry7.get()) >= 11.7 and float(self.entry7.get() <= 13.8)):
                    self.himo = Label(
                        self.report1, text="3).Your haemoglobin level is good", font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                elif (float(self.entry7.get()) > 13.8):
                    self.himo = Label(
                        self.report1, text="3).Your haemoglobin level is quiet high", font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.himo = Label(
                        self.report1, text="3).Your haemoglobin level is low", font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                self.cholestrol_report1()

            def cholestrol_report1(self):
                if (int(self.entry8.get()) >= 125
                        and int(self.entry8.get() <= 200)):
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol is in good level", font=('callibri', 10, 'bold'))
                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)
                elif (int(self.entry8.get()) > 240):
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol level is high", font=('callibri', 10, 'bold'))

                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol level is low", font=('callibri', 10, 'bold'))
                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)

            def bp_report2(self):
                if (int(self.entry4.get()) < 95):
                    self.bp_low_lab = Label(
                        self.report1, text="1).Your Bp Is low", font=('callibri', 10, 'bold'))
                    self.bp_low_lab.pack(side=TOP, anchor='nw', pady=10)
                elif (int(self.entry5.get()) > 145):
                    self.bp_high_lab = Label(
                        self.report1, text="1).Your bp Is high", font=('callibri', 10, 'bold'))
                    self.bp_high_lab.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.bp_nor = Label(self.report1, text="1).Your bp is normal", font=(
                        'callibri', 10, 'bold'))
                    self.bp_nor.pack(side=TOP, anchor='nw', pady=10)
                self.pulse_rt2()

            def pulse_rt2(self):

                if (int(self.entry6.get()) >= 70 and int(self.entry6.get()) <= 100):
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is normal", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)

                elif (int(self.entry6.get()) > 100):
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is quite high", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.puse_rate = Label(
                        self.report1, text="2).Your pulse rate is quite low", font=('callibri', 10, 'bold'))
                    self.puse_rate.pack(side=TOP, anchor='nw', pady=10)
                self.haemoglobin_report2()

            def haemoglobin_report2(self):
                if (float(self.entry7.get()) >= 12.4 and float(self.entry7.get() <= 14.9)):
                    self.himo = Label(
                        self.report1, text="3).Your haemoglobin level is good", font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                elif (float(self.entry7.get()) > 14.9):
                    self.himo = Label(
                        self.report1, text="3).Your haemoglobin level is quiet high", font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.himo = Label(
                        self.report1, text="3).Your haemoglobin level is low", font=('callibri', 10, 'bold'))
                    self.himo.pack(side=TOP, anchor='nw', pady=10)
                self.cholestrol_report2()

            def cholestrol_report2(self):
                if (int(self.entry8.get()) >= 200 and int(self.entry8.get() <= 239)):
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol is in good level", font=('callibri', 10, 'bold'))
                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)
                elif (int(self.entry8.get()) > 240):
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol level is high", font=('callibri', 10, 'bold'))

                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)
                else:
                    self.cholestr = Label(
                        self.report1, text="4).Your cholestrol level is low", font=('callibri', 10, 'bold'))
                    self.cholestr.pack(side=TOP, anchor='nw', pady=10)

            def diet_plans_fun(self):
                self.dyt_win = Toplevel()
                self.dyt_win.title(
                    "Diet Recommendation:-Health Tracker and Recommender System")
                self.dyt_win.geometry('1728x1080')
                self.dyt_lab = Label(self.dyt_win, image=self.dyt_plans)
                self.dyt_lab.pack()

            def re(self):  # result of bmi
                if (float(self.ent1.get()) == 0.0):
                    self.exception1()
                elif (float(self.ent2.get()) == 0.0):
                    self.exception2()
                else:
                    self.res = str(float(self.ent2.get()) / (float(self.ent1.get())) ** 2)
                    self.p3 = PanedWindow(self.bdy)
                    self.p3.pack(pady=40)
                    self.mb = Message(self.p3, text="Your Body Mass Index IS:", width=250, font=(
                        "haettenschweiler", 18), bg="orange")
                    self.mb.pack()
                    self.p3.add(self.mb)
                    self.mr = Message(self.p3, text=self.res + " kg/m^2",
                                      font=("haettenschweiler", 18), bg="violet", width=270)
                    self.mr.pack()
                    self.p3.add(self.mr)

            def exception1(self):
                self.p4 = PanedWindow(self.bdy)
                self.p4.pack(pady=40)
                self.ms = Message(self.p4, text="Height can't be ZERO", width=150, font=(
                    "haettenschweiler", 18), bg="orange")
                self.ms.pack()
                self.p4.add(self.ms)

            def exception2(self):
                self.p4 = PanedWindow(self.bdy)
                self.p4.pack(pady=40)
                self.ms = Message(self.p4, text="Weight can't be ZERO", width=150, font=(
                    "haettenschweiler", 18), bg="orange")
                self.ms.pack()
                self.p4.add(self.ms)

            def exer(self):  # link for the best exercise videos
                webbrowser.open_new("https://www.youtube.com/user/blogilates")

            def wa(self):
                self.winwa = Toplevel()
                self.winwa.title("Weight Analysis:-Health Tracker and Recommender System")
                self.winwa.geometry('1728x1080')
                self.wa1 = ImageTk.PhotoImage(Image.open(r'C:\Users\shivam kumar\Downloads\project_zipFinal\project\WA#.jpg'))
                self.lab = Label(self.winwa, image=self.wa1)
                self.lab.pack()

            def clock(self):
                self.hour = time.strftime("%I")
                self.minute = time.strftime("%M")
                self.second = time.strftime("%S")
                self.am_pm = time.strftime("%p")
                self.day = time.strftime("%A")
                self.label.config(text=self.hour + ":" + self.minute +
                                       ":" + self.second + self.am_pm)

                self.label.after(1000, self.clock)

        obj = abc()

    # functions for the change of the message on the first page
    def update(self):
        self.s.config(text='Stay Safe & Healthy Always',
                      font=('algerian', 36, 'italic bold'), bg="black", fg="light green")
        self.s.after(5000, self.update1)

    def update1(self):
        self.s.config(text='Designed By: ASHISH,SHIVAM,Shubham co. pvt. ltd', font=('algerian', 36), bg="brown",
                      fg="blue")
        self.s.after(5000, self.update2)

    def update2(self):
        self.s.config(text='Health Tracker and Recommender System',
                      font=('algerian', 36, 'italic bold'), bg="green", fg="orange")
        self.s.after(5000, self.update)


man = main1()
