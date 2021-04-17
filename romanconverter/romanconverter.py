from tkinter import *
import re
#output function
def convert():
    #collection of ints as string to check later
    ints = "0123456789"
    #entered text
    entered = textentry.get()
    #clear output
    output.delete(0.0, END)
    #make entered uppercase if not already
    entered = entered.upper()
    #dictionary of roman numerals converted to integers
    toint = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    #dictionary of integers converted to roman numerals
    torom = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    #initialize counters
    intcount = 0
    romcount = 0
    #check how many integers or roman numerals there are
    for x in entered:
        #output is "please enter valid" if a non-int or roman is found
        if x == "" or (x not in ints and x not in toint):
            out = "Please enter a valid roman numeral or integer."
            break
        #count roman numerals
        elif x in toint:
            romcount += 1
        #count integers
        elif x in ints:
            intcount += 1
    #check if integer count is equal to length of entered text to ensure that user did not entere mixed number (i.e. both arabic and roman)
    if intcount == len(entered) and len(entered) > 0:
        out = ""
        #make entered integer
        intered = int(entered)
        for x in reversed(sorted(torom.keys())):
            while x <= intered:
                intered = intered - x
                out += torom[x]
    #check if roman count is equal to length of entered text to ensure that user did not entere mixed number (i.e. both arabic and roman)
    elif romcount == len(entered) and len(entered) > 0:
        #regex to check if roman numeral is valid
        if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", entered):
            temp = 0
            out = 0
            for x in list(entered)[::-1]:
                if temp == 0:
                    out += toint[x]
                elif temp > toint[x]:
                    out -= toint[x]
                else:
                    out += toint[x]
                temp = toint[x]
        #if not valid roman, output is "please enter valid"
        else:
           out = "Please enter a valid roman numeral or integer."
    else:
        out = "Please enter a valid roman numeral or integer."
    output.insert(END, out)
#window close
def close():
    window.destroy()
#window config
window = Tk()
window.title("Roman numeral converter")
window.iconbitmap("roman.ico")
window.configure(bg = "#F2F4F3", padx = "5", pady = "5")
window.resizable(0, 0)
#frame config
frame = Frame(window, padx = "5", pady = "5")
#label
Label(window, text = "Enter a roman numeral or an integer to convert. Accepts roman numerals from 1 to 3999.", bg = "#F2F4F3", fg = "#0A0908", font = "none 11").grid(row = 0, column = 0, sticky = W)
#text entry
Label(window, text = "", bg = "#F2F4F3", fg = "#0A0908", font = "none 1").grid(row = 1, column = 0, sticky = W)
textentry = Entry(window, width = 95, bg = "#F2F4F3", fg = "#0A0908")
textentry.grid(row = 2, column = 0, sticky = W)
#enter button
Label(window, text = "", bg = "#F2F4F3", fg = "#0A0908", font = "none 1").grid(row = 3, column = 0, sticky = W)
Button(window, text = "Convert", width = 8, command = convert, relief = "flat", bg = "#A9927D", fg = "#F2F4F3", borderwidth = "0", activebackground = "#A9927D", activeforeground = "#F2F4F3").grid(row = 4, column = 0, sticky = W)
#text box
Label(window, text = "", bg = "#F2F4F3", fg = "#0A0908", font = "none 1").grid(row = 5, column = 0, sticky = W)
output = Text(window, width = 71, height = 5, wrap = WORD, bg = "#F2F4F3", fg = "#0A0908")
output.grid(row = 6, column = 0, columnspan = 2, sticky = W)
#exit
Label(window, text = "", bg = "#F2F4F3", fg = "#0A0908", font = "none 1").grid(row = 7, column = 0, sticky = W)
Button(window, text = "Quit", width = 8, command = close, relief = "flat", bg = "#49111C", fg = "#F2F4F3", borderwidth = "0", activebackground = "#49111C", activeforeground = "#F2F4F3").grid(row = 8, column = 0, columnspan = 2, sticky = W)
#create window
window.mainloop()