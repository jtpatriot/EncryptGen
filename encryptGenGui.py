# Password Generator
# 
# 
# 
#
#
import random
from Tkinter import *
import ttk


def printBlankLine(amount):
	while amount >> 0:
		print ''
		amount = amount - 1


def replacerDict():
	replacers = {' ':'', 'a':'@', 'e':'3', 'o':'0', 's':'5', 't':'7'}
	return replacers


def stringInput():
	print 'What is the word you want to be turned into a password?'
	string = raw_input('Input word or phrase: ')
	return string


def charReplace(text, dic):
	for i, j in dic.iteritems():
		text = text.replace(i, j)
	return text


def printResults(results):
	print 'The secured string is:', results


def security_level(number):
    try:
        int(number)
	while int(number) not in range(1,10001):
	    number = raw_input('Enter a number: ')
	    number = int(number)
	    loop = 0
    except ValueError:
	number = raw_input('Enter a number: ')
    return number
		

def security_chars(number):
    # Character Strings
    pass_chars = '0'
    hex_string_low = '0123456789abcdef'
    alphabet_string_low = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_string_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_string_low_up = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit_string = '0123456789'
    symbol_string = """!@#$%^&*()"""
    at_pound_string = """@#"""
    
    if number == 1:
        pass_chars = hex_string_low
        print hex_true_str
                    
    elif number == 2:
        pass_chars = alphabet_string_low
        print alph_low_true_str
                    
    elif number == 3:
        pass_chars = alphabet_string_up
        print alph_up_true_str

    return pass_chars


# Ask for symbols eventually...

def generate_passphrase(characters, length):
	listChars = [random.choice(characters) for n in xrange(length)]
	result = "".join(listChars)
	print 'Passphrase with ', str(length), 'characters: ', result, ''



root = Tk()
root.title("EncryptGen")

mainframe = ttk.Frame(root, padding="3 3 12 12", width=600, height=300)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(1)
mainframe.columnconfigure(2, weight=4)
mainframe.rowconfigure(2)
mainframe.rowconfigure(3)
mainframe.rowconfigure(4)
mainframe.rowconfigure(5)
mainframe.grid_propagate(0)

password = StringVar()
printStr = StringVar()
description = StringVar()

description.set("""Modes:\n"""\
"""1) Generate a random character password.\n"""\
"""2) Randomize a specific word or phrase.\n"""\
"""3) Combination of 1 and 2.""")

printStr.set('')

password_entry = ttk.Entry(mainframe, width=7, textvariable=password)
password_entry.grid(column=2, row=3, sticky=(W, E, N))

ttk.Entry(mainframe, textvariable=printStr).grid(column=2, row=5, sticky=(W, E, N))

ttk.Button(mainframe, text="Mode 1", command='').grid(column=2, row=1, sticky=(W, N))
ttk.Button(mainframe, text="Mode 2", command='').grid(column=2, row=1, sticky=(N))
ttk.Button(mainframe, text="Mode 3", command='').grid(column=2, row=1, sticky=(E, N))

ttk.Checkbutton(mainframe, text="numbers", command=security_chars(1)).grid(column=2, row=4, sticky=(W, N))
ttk.Checkbutton(mainframe, text="lowercase", command=security_chars(2)).grid(column=2, row=4, sticky=(N))
ttk.Checkbutton(mainframe, text="uppercase", command=security_chars(3)).grid(column=2, row=4, sticky=(E, N))


ttk.Label(mainframe, textvariable=description).grid(column=2, row=2, sticky=NW)
ttk.Label(mainframe, text="Number of\nCharacters:").grid(column=1, row=3, sticky=NW)
ttk.Button(mainframe, text="Generate").grid(column=1, row=5, sticky=NW)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

password_entry.focus()
root.bind('<Return>', '')

root.mainloop()


