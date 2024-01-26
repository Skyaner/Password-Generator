from tkinter import *
import random

def generate_password():
    try:
        length = int(entry_length.get())
    except:
        entry_length.insert(0,"Invalid Input: ")
    
      
    
    Digit = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    cletter = ("Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "Y", "X", "C", "V", "B", "N", "M")
    letter = ("q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "y", "x", "c", "v", "b", "n", "m")
    symbol = ("^", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "ß", "\\", "+", "*", "<", ">", "|", "'", "#", ",", ";", ":", "-", "_", "{", "}", "[", "]", "~")
    
    password = ""
    for i in range(length):
        password += random.choice(Digit + cletter + letter + symbol)           
    
    
    entry_password = Entry(root)
    entry_password.insert(0,password)
    entry_password.config(state="read")
    entry_password.grid(row=2,column=1)
    
    return entry_password
   
    
def delet():
    entry_length.delete(0,END)   
    

root = Tk()
root.geometry("500x200")
root.title("Password Generator")
root.resizable(0,0)


#Description
Label(root, text="This programm will generate a passwort for you.").grid(row=0)


Label(root, text="Please enter a length for your password.").grid(row=1, column=0)
entry_length = Entry(root)
entry_length.grid(row=1, column=1)

Label(root, text="Password").grid(row=2, column=0)

Button(root, text="Quit", command=root.quit).grid(row=5, column=0)
Button(root, text="Generate", command=generate_password).grid(row=5, column=1)
Button(root, text="Delete", command=delet).grid(row=5, column=2)



root.mainloop()