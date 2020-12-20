#tkinter is used for gui
from tkinter import *
window=Tk("currency converter")

def from_rs():
    # convert rs
    USD= float(e2_value.get()) * 0.0134934556739981
    EUR=float(e2_value.get()) * 0.011
    yuan=float(e2_value.get()) * 1.41
    YEN= float(e2_value.get()) * 0.71
    GBP= float(e2_value.get()) * 0.010
    CFH= float(e2_value.get()) * 0.012
    CAD = float(e2_value.get()) * 0.018
    ZAR= float(e2_value.get()) * 0.21
    RS= float(e2_value.get()) * 1


    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_usd():
    # convert united ststes dollar
    USD= float(e2_value.get()) * 1
    EUR=float(e2_value.get()) * 0.84
    yuan=float(e2_value.get()) * 6.65
    YEN= float(e2_value.get()) * 104.62
    GBP= float(e2_value.get()) * 0.75
    CFH= float(e2_value.get()) * 0.91
    CAD = float(e2_value.get()) * 1.31
    ZAR= float(e2_value.get()) * 15.37
    RS= float(e2_value.get()) * 74.11


    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_eur():
    # conver euro
    USD= float(e2_value.get()) * 1.19
    EUR=float(e2_value.get()) * 1
    yuan=float(e2_value.get()) * 7.81
    YEN= float(e2_value.get()) * 124.03
    GBP= float(e2_value.get()) * 0.89
    CFH= float(e2_value.get()) * 1.08
    CAD = float(e2_value.get()) * 1.31
    ZAR= float(e2_value.get()) * 1.55
    RS= float(e2_value.get()) * 84.81


    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_yuan():
    # convert to chinnes yuan
    USD= float(e2_value.get()) * 0.15
    EUR=float(e2_value.get()) * 0.13
    yuan=float(e2_value.get()) * 1
    YEN= float(e2_value.get()) * 15.88
    GBP= float(e2_value.get()) * 0.11
    CFH= float(e2_value.get()) * 0.14
    CAD = float(e2_value.get()) * 0.20
    ZAR= float(e2_value.get()) * 2.33
    RS= float(e2_value.get()) * 11.24


    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_yen():
    # convert to japanes yen
    USD= float(e2_value.get()) * 0.0096
    EUR=float(e2_value.get()) * 0.0081
    yuan=float(e2_value.get()) * 0.063
    YEN= float(e2_value.get()) * 1
    GBP= float(e2_value.get()) * 0.0072
    CFH= float(e2_value.get()) * 0.0087
    CAD = float(e2_value.get()) * 0.012
    ZAR= float(e2_value.get()) * 0.15
    RS= float(e2_value.get()) * 0.71


    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_gbp():
    # convert to pound
    USD= float(e2_value.get()) *1.33
    EUR=float(e2_value.get()) * 1.11
    yuan=float(e2_value.get()) * 8.78
    YEN= float(e2_value.get()) * 139.52
    GBP= float(e2_value.get()) * 1.0000000000
    CFH= float(e2_value.get()) * 1.22
    CAD = float(e2_value.get()) * 1.74
    ZAR= float(e2_value.get()) * 20.43
    RS= float(e2_value.get()) * 98.70

    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_chf():
    # convrt to swiss France
    USD= float(e2_value.get()) * 1.10
    EUR=float(e2_value.get()) * 0.95
    yuan=float(e2_value.get()) * 7.23
    YEN= float(e2_value.get()) * 114.80
    GBP= float(e2_value.get()) * 0.82
    CFH= float(e2_value.get()) * 1.000000000000
    CAD = float(e2_value.get()) * 1.43
    ZAR= float(e2_value.get()) * 16.81
    RS= float(e2_value.get()) * 81.25

    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_cad():
    # convert to canadin Dollar
    USD= float(e2_value.get()) * 0.77
    EUR=float(e2_value.get()) * 0.65
    yuan=float(e2_value.get()) * 5.06
    YEN= float(e2_value.get()) * 80.27
    GBP= float(e2_value.get()) * 0.57
    CFH= float(e2_value.get()) * 0.70
    CAD = float(e2_value.get()) * 1
    ZAR= float(e2_value.get()) * 11.75
    RS= float(e2_value.get()) * 56.82

    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)


def from_zar():
    # converted to south african rand
    USD= float(e2_value.get()) * 0.065
    EUR=float(e2_value.get()) * 0.055
    yuan=float(e2_value.get()) * 0.43
    YEN= float(e2_value.get()) * 6.84
    GBP= float(e2_value.get()) * 0.049
    CFH= float(e2_value.get()) * 0.060
    CAD = float(e2_value.get()) * 0.85
    ZAR= float(e2_value.get()) * 1
    RS= float(e2_value.get()) * 4.84

    t1.delete("1.0",END)
    t1.insert(END, USD)
    t2.delete("1.0", END)
    t2.insert(END, EUR)
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    t4.delete("1.0", END)
    t4.insert(END, YEN)
    t5.delete("1.0", END)
    t5.insert(END, GBP)
    t6.delete("1.0", END)
    t6.insert(END, CFH)
    t7.delete("1.0", END)
    t7.insert(END, CAD)
    t8.delete("1.0", END)
    t8.insert(END, ZAR)
    t9.delete("1.0", END)
    t9.insert(END, RS)

#labels
e1 = Label(window, text="Enter the amount")
e = Label(window, text="CONVERTED INTO----")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='USD')
e4 = Label(window, text='EUR')
e5 = Label(window, text='YUAN')
e6 = Label(window, text='YEN')
e7 = Label(window, text='GBP')
e8 = Label(window, text='CFH')
e9 = Label(window, text='CAD')
e10= Label(window, text='ZAR')
e11= Label(window, text='RS')

#output grid layout
t1 = Text(window,height=1,width=30)
t2 = Text(window, height=1, width=30)
t3 = Text(window, height=1, width=30)
t4 = Text(window, height=1, width=30)
t5 = Text(window, height=1, width=30)
t6 = Text(window, height=1, width=30)
t7 = Text(window, height=1, width=30)
t8 = Text(window, height=1, width=30)
t9 = Text(window, height=1, width=30)

#buttons
b1=Button(window,text="     Rs         ",command=from_rs)
b1.grid(row=1, column=6)

b2=Button(window,text="     USD        ",command=from_usd)
b2.grid(row=1, column=5)

b3=Button(window,text="     EUR      ",command=from_eur)
b3.grid(row=1, column=7)

b4=Button(window,text="     YUAN   ",command=from_yuan)
b4.grid(row=2, column=7)

b5=Button(window,text="     YEN       ",command=from_yen)
b5.grid(row=2, column=5)

b6=Button(window,text="     GBP     ",command=from_gbp)
b6.grid(row=2, column=6)

b7=Button(window,text="     CHF        ",command=from_chf)
b7.grid(row=3, column=5)

b8=Button(window,text="     CAD     ",command=from_cad)
b8.grid(row=3, column=6)

b9=Button(window,text="     ZAR       ",command=from_zar)
b9.grid(row=3, column=7)





#grid
e.grid(row=0, column=4)
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=2, column=0)
t1.grid(row=3, column=0)
e4.grid(row=2, column=1)
t2.grid(row=3, column=1)
e5.grid(row=2, column=2)
t3.grid(row=3, column=2)

e6.grid(row=4, column=0)
t4.grid(row=5, column=0)
e7.grid(row=4, column=1)
t5.grid(row=5, column=1)
e8.grid(row=4, column=2)
t6.grid(row=5, column=2)

e9.grid(row=6, column=0)
t7.grid(row=7, column=0)
e10.grid(row=6, column=1)
t8.grid(row=7, column=1)
e11.grid(row=6, column=2)
t9.grid(row=7, column=2)

#to hold output
window.mainloop()