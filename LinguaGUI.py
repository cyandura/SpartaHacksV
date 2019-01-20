from tkinter import *

m = Tk() #m is the name of the object

frame = Frame(m)
frame.pack()

recordframe = Frame(m)
saveandconvertframe = Frame(m)
gridframe = Frame(recordframe)

menu = Menu(m)
m.config(menu=menu)
filemenu = Menu(m)
menu.add_cascade(label='File', menu = filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Exit', command=m.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='help', menu=helpmenu)
helpmenu.add_command(label='About')

v = IntVar()
recordtime="default"
filenametxt=""

minutes=0
seconds=0

#recordframe
Label(recordframe,text='Recording Time in Minutes:').grid(row=0, column=0)
Label(recordframe, text='File Name:').grid(row=1, column=0)
filename1 = Entry(recordframe, textvariable=filenametxt, width=35)

#gridframe in within recordframe
minutesentry = Entry(gridframe,  width=16)
secondsentry = Entry(gridframe,  width=16)

minutesentry.insert(END, '0')
secondsentry.insert(END, '0')

#convertframe
Label(saveandconvertframe, text='File Name:').grid(row=0, column=0)
filename = Entry(saveandconvertframe, text='File Name: ', width=35)


record = Button(recordframe, text='Record->Convert', command = lambda : recordbtn(recordtime), width=35)
stop = Button(recordframe, text='Stop', width=35)
Start = Button(m, text='Start', width=40)
share = Button(m, text='Share', width=40)
saveas = Button(saveandconvertframe, text='Save As', width=40)
convert = Button(saveandconvertframe, text='Convert', width=40)


stop.grid(row=3,column=0)
record.grid(row=3, column=1)
filename.grid(row=0, column=1)

minutesentry.pack(side = LEFT)
Label(gridframe, text=':').pack(side= LEFT)
secondsentry.pack(side = LEFT)

filename1.grid(row=1, column=1)

gridframe.grid(row=0,column=1)


convert.grid(row=3)
saveas.grid(row=3,column=1)

def recordmenu():
    recordframe.pack(side = LEFT)

    saveandconvertframe.pack_forget()
    return

def saveandconvertmenu():
    recordframe.pack_forget()
    saveandconvertframe.pack(side = LEFT)
    return

def pdf():
    return
def docx():
    return
def txt():
    return

def recordbtn(time):

    minutes = int(minutesentry.get())*60
    seconds = int(secondsentry.get())
    print(minutes+seconds)

    return

def stopbtn():
    return
def convertbtn():
    return
def saveasbtn():
    return

R1 = Radiobutton(m, text='Record', variable=v, value=1, command = lambda : recordmenu()).pack(anchor=W)
R2 = Radiobutton(m, text='Convert', variable=v, value=2,command = lambda : saveandconvertmenu()).pack(anchor=W)

R3 = Radiobutton(saveandconvertframe, text='.PDF', variable=v, value=3, command = lambda : pdf()).grid(row=1,column=0)
R4 = Radiobutton(saveandconvertframe, text='.DOCX', variable=v, value=4,command = lambda : docx()).grid(row=1,column=1)
R5 = Radiobutton(saveandconvertframe, text='.TXT', variable=v, value=5,command = lambda : txt()).grid(row=1,column=2)

R6 = Radiobutton(recordframe, text='.PDF', variable=v, value=6, command = lambda : pdf()).grid(row=2,column=0)
R7 = Radiobutton(recordframe, text='.DOCX', variable=v, value=7,command = lambda : docx()).grid(row=2,column=1)
R8 = Radiobutton(recordframe, text='.TXT', variable=v, value=8,command = lambda : txt()).grid(row=2,column=2)


m.mainloop()
