# Password Generator
# 
# 
import random
from Tkinter import *
import ttk


def replacerDict():
    replacers = {' ':'', 'a':'@', 'e':'3', 'o':'0', 's':'5', 't':'7'}
    return replacers


def stringInput():
    print ''


def charReplace(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
        return text


def security_level(number):
    try:
        number = int(number)
        endNumber.set(number)
    except:
        printStr.set('Please enter a number above.')
    return endNumber
        

def containStrings():
    pass_chars = StringVar('')
    if(check1.get() == 1):
        print "check1 is on"
        pass_chars.set('1234567890')
    if(check2.get() == 1):
        print "check2 is on"
        pass_chars.set('abcdefghijklmnopqrstuvwxyz')
    if(check3.get() == 1):
        print "check3 is on"
        pass_chars.set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return pass_chars


def randomizeJoin(x, y):
    y = int(y) # ValueError: invalid literal for int() with base 10: 'PY_VAR8'
    listed = [random.choice(x) for n in xrange(y)]
    results = "".join(listed)
    printStr.set(results)



def generate():    
    passChars.set(containStrings())
    length.set(security_level(numCount.get()))
    randomizeJoin(passChars.get(), length.get())


root = Tk()
root.title("EncryptGen")

mainframe = ttk.Frame(root, padding="3 3 12 12", width=500, height=300)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(1)
mainframe.columnconfigure(2, weight=4)
mainframe.rowconfigure(2)
mainframe.rowconfigure(3)
mainframe.rowconfigure(4)
mainframe.rowconfigure(5)
mainframe.grid_propagate(0)

numCount = StringVar('')
printStr = StringVar('')
description = StringVar('')

check1 = IntVar(0)
check2 = IntVar(0)
check3 = IntVar(0)

length = StringVar('')
passChars = StringVar('')

endNumber = IntVar()

description.set("""Modes:\n"""\
"""1) Generate a random character password.\n"""\
"""2) Randomize a specific word or phrase.\n"""\
"""3) Combination of 1 and 2.""")

printStr.set('')

numCount_entry = ttk.Entry(mainframe, width=20, textvariable=numCount)
numCount_entry.grid(column=2, row=3, sticky=(W, E, N))

ttk.Entry(mainframe, textvariable=printStr).grid(column=2, row=5, sticky=(W, E, N))

ttk.Button(mainframe, text="Mode 1", command='').grid(column=2, row=1, sticky=(W, N))
ttk.Button(mainframe, text="Mode 2", command='').grid(column=2, row=1, sticky=(N))
ttk.Button(mainframe, text="Mode 3", command='').grid(column=2, row=1, sticky=(E, N))

ttk.Checkbutton(mainframe, text="Numbers", variable=check1).grid(column=2, row=4, sticky=(W, N))
ttk.Checkbutton(mainframe, text="Lowercase", variable=check2).grid(column=2, row=4, sticky=(N))
ttk.Checkbutton(mainframe, text="Uppercase", variable=check3).grid(column=2, row=4, sticky=(E, N))


ttk.Label(mainframe, textvariable=description).grid(column=2, row=2, sticky=NW)
ttk.Label(mainframe, text="Number of\nCharacters:").grid(column=1, row=3, sticky=NW)
ttk.Button(mainframe, text="Generate", command=generate).grid(column=1, row=5, sticky=NW)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

numCount_entry.focus()
root.bind('<Return>', generate)

root.mainloop()


