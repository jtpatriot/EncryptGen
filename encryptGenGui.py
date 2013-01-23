# Password Generator
# 
# 
import random
from Tkinter import *
import ttk


### Set the Displayed Widgets
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
    numCount_entry.focus()
def displayMode2():
    removeMode1()
    removeMode3()
    textToMix_label.grid(column=1, row=1, sticky=(W, N))
    mode2Generate.grid(column=1, row=2, sticky=(W, N))
    textToMix_entry.grid(column=2, row=1, sticky=(W, E))
    mode2Result_box.grid(column=2, row=2, sticky=(W, E, N))
def displayMode3():
    removeMode1()
    removeMode2()
    mode3Input1_label.grid(column=1, row=1, sticky=(W, N))
    mode3Generate.grid(column=1, row=2, sticky=(W, N))
    mode3Input1_entry.grid(column=2, row=1, sticky=(W, E))
    mode3Result_box.grid(column=2, row=2, sticky=(W, E, N))
####################
    

### Remove Deselected Widgets
def removeMode1():
    numCount_entry.grid_remove()
    numCount_label.grid_remove()
    mode1Check1.grid_remove()
    mode1Check2.grid_remove()
    mode1Check3.grid_remove()
    mode1Generate.grid_remove()
    mode1Results.grid_remove()
def removeMode2():
    textToMix_label.grid_remove()
    mode2Generate.grid_remove()
    textToMix_entry.grid_remove()
    mode2Result_box.grid_remove()
def removeMode3():
    mode3Input1_label.grid_remove()
    mode3Generate.grid_remove()
    mode3Input1_entry.grid_remove()
    mode3Result_box.grid_remove()
####################


### Mode 1 Functions
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
####################


### Mode 2 Functions
def replacerDict():
    replacers = {' ':'', 'a':'@', 'e':'3', 'o':'0', 's':'5', 't':'7'}
    return replacers
def charReplace(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
####################


### Generate Results Functions
def generateMode1():    
    passChars.set(containStrings(check1.get(), check2.get(), check3.get()))
    length.set(security_level(numCount.get()))
    printStr.set(randomizeJoin(passChars.get(), length.get()))
def generateMode2():    
    mode2results.set(charReplace(str(textToMix.get()), replacerDict()))
def generateMode3():
    mode3results.set('Mode 3 is not functional yet.')
####################


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
modeframe.grid(column=1, row=3, sticky=(W, E, S))
modeframe.grid_propagate(0)

mode1Button = ttk.Button(mainframe, text="Mode 1", command=displayMode1)
mode1Button.grid(column=1, row=1, sticky=(W, N))
mode2Button = ttk.Button(mainframe, text="Mode 2", command=displayMode2)
mode2Button.grid(column=1, row=1, sticky=(N))
mode3Button = ttk.Button(mainframe, text="Mode 3", command=displayMode3)
mode3Button.grid(column=1, row=1, sticky=(E, N))

description = StringVar('')
description.set("""Modes:\n"""\
"""1) Generate a random character password.\n"""\
"""2) Randomize a specific word or phrase.\n"""\
"""3) Combination of 1 and 2.""")
descriptionLabel = ttk.Label(mainframe, textvariable=description)
descriptionLabel.grid(column=1, row=2, sticky=N)


### Mode 1 variables
numCount = StringVar('')
printStr = StringVar('')
check1 = IntVar(0)
check2 = IntVar(0)
check3 = IntVar(0)
length = IntVar()
passChars = StringVar('')
endNumber = IntVar()
####################

### Mode 2 variables
textToMix = StringVar('')
mode2results = StringVar('')
####################

### Mode 3 variables
textInputMode3 = StringVar('')
mode3results = StringVar('')
####################


### Mode 1 objects
numCount_entry = ttk.Entry(modeframe, width=42, textvariable=numCount)
numCount_label = ttk.Label(modeframe, text="Number of\nCharacters:")
mode1Check1 = ttk.Checkbutton(modeframe, text="Numbers", variable=check1)
mode1Check2 = ttk.Checkbutton(modeframe, text="Lowercase", variable=check2)
mode1Check3 = ttk.Checkbutton(modeframe, text="Uppercase", variable=check3)
mode1Generate = ttk.Button(modeframe, text="Generate", command=generateMode1)
mode1Results = ttk.Entry(modeframe, textvariable=printStr)
##################

### Mode 2 objects
textToMix_entry = ttk.Entry(modeframe, width=42, textvariable=textToMix)
textToMix_label = ttk.Label(modeframe, text="Word or Phrase\nto scramble:")
mode2Result_box = ttk.Entry(modeframe, textvariable=mode2results)
mode2Generate = ttk.Button(modeframe, text="Scramble", command=generateMode2)
##################

### Mode 3 objects
mode3Input1_entry = ttk.Entry(modeframe, width=42, textvariable=textInputMode3)
mode3Input1_label = ttk.Label(modeframe, text="Word or Phrase\nto scramble:")
mode3Result_box = ttk.Entry(modeframe, textvariable=mode3results)
mode3Generate = ttk.Button(modeframe, text="Generate", command=generateMode3)
##################


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#root.bind('<Return>', generate)

root.mainloop()


