# Password Generator
# 
# 
import random
from Tkinter import *
import ttk


def displayMode1():
    removeMode2()
    removeMode3()
    numCount_entry.grid(column=2, row=1, sticky=(W, E, N))
    numCount_label.grid(column=1, row=1, sticky=NW)
    mode1Check1.grid(column=2, row=2, sticky=(W, N))
    mode1Check2.grid(column=2, row=2, sticky=(N))
    mode1Check3.grid(column=2, row=2, sticky=(E, N))
    mode1Generate.grid(column=1, row=3, sticky=NW)
    mode1Results.grid(column=2, row=3, sticky=(W, E, N))
    

def displayMode2():
    removeMode1()
    removeMode3()
    

def displayMode3():
    removeMode1()
    removeMode2()
    

def removeMode1():
    numCount_entry.grid_remove()
    numCount_label.grid_remove()
    mode1Check1.grid_remove()
    mode1Check2.grid_remove()
    mode1Check3.grid_remove()
    mode1Generate.grid_remove()
    mode1Results.grid_remove()


def removeMode2():
    print ''


def removeMode3():
    print ''


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

modeframe = ttk.Frame(mainframe, padding="3 3 12 12", width=480, height=200)
#mode2frame = ttk.Frame(mainframe, padding="3 3 12 12", width=480, height=200)
#mode3frame = ttk.Frame(mainframe, padding="3 3 12 12", width=480, height=200)

modeframe.grid(column=1, row=3, sticky=(W, E, S))

modeframe.grid_propagate(0)

numCount = StringVar('')
printStr = StringVar('')
description = StringVar('')

check1 = IntVar(0)
check2 = IntVar(0)
check3 = IntVar(0)
check4 = IntVar(0)

length = IntVar()
passChars = StringVar('')

endNumber = IntVar()

description.set("""Modes:\n"""\
"""1) Generate a random character password.\n"""\
"""2) Randomize a specific word or phrase.\n"""\
"""3) Combination of 1 and 2.""")

printStr.set('')


mode1Button = ttk.Button(mainframe, text="Mode 1", command=displayMode1)
mode1Button.grid(column=1, row=1, sticky=(W, N))
mode2Button = ttk.Button(mainframe, text="Mode 2", command=displayMode2)
mode2Button.grid(column=1, row=1, sticky=(N))
mode3Button = ttk.Button(mainframe, text="Mode 3", command=displayMode3)
mode3Button.grid(column=1, row=1, sticky=(E, N))

descriptionLabel = ttk.Label(mainframe, textvariable=description)
descriptionLabel.grid(column=1, row=2, sticky=N)


### Mode 1 objects         ###
numCount_entry = ttk.Entry(modeframe, width=42, textvariable=numCount)
numCount_label = ttk.Label(modeframe, text="Number of\nCharacters:")

mode1Check1 = ttk.Checkbutton(modeframe, text="Numbers", variable=check1)
mode1Check2 = ttk.Checkbutton(modeframe, text="Lowercase", variable=check2)
mode1Check3 = ttk.Checkbutton(modeframe, text="Uppercase", variable=check3)

mode1Generate = ttk.Button(modeframe, text="Generate", command=generate)
mode1Results = ttk.Entry(modeframe, textvariable=printStr)
###############################




for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

numCount_entry.focus()
root.bind('<Return>', generate)

root.mainloop()



