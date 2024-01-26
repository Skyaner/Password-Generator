from tkinter import *
import random

def generate_password():
    try:
        length = int(entry_length.get())
    except:
        Label(root, text="Please enter a Integer for the length of your password.").grid(row=2, column=0)
        
    Digit = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    cletter = ("Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "Y", "X", "C", "V", "B", "N", "M")
    letter = ("q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "y", "x", "c", "v", "b", "n", "m")
    symbol = ("^", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "ß", "\\", "+", "*", "<", ">", "|", "'", "#", ",", ";", ":", "-", "_", "{", "}", "[", "]", "~")
    
    password = ""
    for i in range(length):
        password += random.choice(Digit + cletter + letter + symbol)
            
    Label(root, text=f"{password}").grid(row=2, column=0)
    

root = Tk()
root.geometry("400x200")
root.title("Password Generator")
root.resizable(0,0)


#Description
Label(root, text="This programm will generat a passwort for you.").grid(row=0)


Label(root, text="Please enter a length for your password.").grid(row=1, column=0)
entry_length = Entry(root)
entry_length.grid(row=1, column=1)


Button(root, text="Quit", command=root.quit).grid(row=5, column=0)
Button(root, text="generate", command=generate_password).grid(row=5, column=1)


root.mainloop()