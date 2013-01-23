# Password Generator
# 
# 
import random
from Tkinter import *
import ttk


def displayMode(number):
    if number == 1:
        mode2frame.grid_remove()
        mode3frame.grid_remove()
        mode1frame.grid()
    if number == 2:
        mode3frame.grid_remove()
        mode1frame.grid_remove()
        mode2frame.grid(column=1, row=3, sticky=(N, W, E, S))
    if number == 3:
        mode2frame.grid_remove()
        mode1frame.grid_remove()
        mode3frame.grid(column=1, row=3, sticky=(N, W, E, S))


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
    return endNumber.get()
        

def containStrings(check1, check2, check3):
    pass_chars = StringVar('')
    if(check1 == 1):
        pass_chars.set(pass_chars.get() + '1234567890')
    if(check2 == 1):
        pass_chars.set(pass_chars.get() + 'abcdefghijklmnopqrstuvwxyz')
    if(check3 == 1):
        pass_chars.set(pass_chars.get() + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return pass_chars.get()


def randomizeJoin(x, y):
    try:
        listed = [random.choice(x) for n in xrange(y)]
        results = "".join(listed)
        return results
    except IndexError:
        return 'Error: Please make a checkbox selection.'



def generate():    
    passChars.set(containStrings(check1.get(), check2.get(), check3.get()))
    length.set(security_level(numCount.get()))
    printStr.set(randomizeJoin(passChars.get(), length.get()))


root = Tk()
root.title("EncryptGen")

mainframe = ttk.Frame(root, padding="3 3 12 12", width=500, height=300)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(1)
mainframe.rowconfigure(1)
mainframe.rowconfigure(2)
mainframe.rowconfigure(3)
mainframe.grid_propagate(0)

mode1frame = ttk.Frame(mainframe, padding="3 3 12 12", width=480, height=200)
#mode2frame = ttk.Frame(mainframe, padding="3 3 12 12", width=480, height=200)
#mode3frame = ttk.Frame(mainframe, padding="3 3 12 12", width=480, height=200)

mode1frame.grid(column=1, row=3, sticky=(W, E, S))

mode1frame.grid_propagate(0)

numCount = StringVar('')
printStr = StringVar('')
description = StringVar('')

check1 = IntVar(0)
check2 = IntVar(0)
check3 = IntVar(0)

length = IntVar()
passChars = StringVar('')

endNumber = IntVar()

description.set("""Modes:\n"""\
"""1) Generate a random character password.\n"""\
"""2) Randomize a specific word or phrase.\n"""\
"""3) Combination of 1 and 2.""")

printStr.set('')



mode1Results = ttk.Entry(mode1frame, textvariable=printStr)
mode1Results.grid(column=2, row=3, sticky=(W, E, N))

mode1Button = ttk.Button(mainframe, text="Mode 1", command='')
mode1Button.grid(column=1, row=1, sticky=(W, N))
mode2Button = ttk.Button(mainframe, text="Mode 2", command='')
mode2Button.grid(column=1, row=1, sticky=(N))
mode3Button = ttk.Button(mainframe, text="Mode 3", command='')
mode3Button.grid(column=1, row=1, sticky=(E, N))

descriptionLabel = ttk.Label(mainframe, textvariable=description)
descriptionLabel.grid(column=1, row=2, sticky=N)

numCount_entry = ttk.Entry(mode1frame, width=42, textvariable=numCount)
numCount_entry.grid(column=2, row=1, sticky=(W, E, N))
numCount_label = ttk.Label(mode1frame, text="Number of\nCharacters:")
numCount_label.grid(column=1, row=1, sticky=NW)


mode1Check1 = ttk.Checkbutton(mode1frame, text="Numbers", variable=check1)
mode1Check1.grid(column=2, row=2, sticky=(W, N))
mode1Check2 = ttk.Checkbutton(mode1frame, text="Lowercase", variable=check2)
mode1Check2.grid(column=2, row=2, sticky=(N))
mode1Check3 = ttk.Checkbutton(mode1frame, text="Uppercase", variable=check3)
mode1Check3.grid(column=2, row=2, sticky=(E, N))


mode1Generate = ttk.Button(mode1frame, text="Generate", command=generate)
mode1Generate.grid(column=1, row=3, sticky=NW)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

numCount_entry.focus()
root.bind('<Return>', generate)

root.mainloop()



