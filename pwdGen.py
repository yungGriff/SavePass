#import PyDictionary
import random
import string
import sys
import tkinter as tk
import pyperclip
import tkinter.messagebox as messagebox


def window():
    global result_text
    global result_label
    app = tk.Tk()
    app.title("Pzzzwrd")
    #App geometry
    window_width = 400
    window_height = 200
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    label = tk.Label(app, text="Password")
    label.pack()


    button = tk.Button(app, text="Generate", command=on_button_click)
    button.pack()

    result_label = tk.Label(app, text="Your generated password is: \n")
    result_label.pack()

    result_text = tk.Text(app, height=2, wrap=tk.WORD)
    result_text.pack()

    app.mainloop()
def on_button_click():
    password = passworded()
    result_text.delete(1.0, tk.END)
    result_label.config(text="Your generated password is: \n")
    result_text.insert(tk.END, password)
    #result_label.config(text="Your generated password is: " + "\n" + password)

def copy_to_clipboard():
    #password = result_label.cget("text").split(":\n")[1]
    password = result_text.get("2.0", tk.END).strip()
    #app.clipboard_clear()
    app.clipboard_append(password)
    pyperclip.copy(password)
   # messagebox.showinfo("Password Copied", "Password copied to clipboard!")
def passworded():
    print("Your generated password is: ")
    functionList = [lowercase() + uppercase() + numbers() + symbols()]
    random.shuffle(functionList)
    password = lowercase() + uppercase() + numbers() + symbols()
    return password

def lowercase():
    lowercaseString = []
    for i in range(0, 3):
        lowercaseString.append(random.choice(string.ascii_lowercase))
    pw_lcString = map(str, lowercaseString)
    pw_lcString = ''.join(pw_lcString)
    return pw_lcString
def uppercase():
    uppercaseString = []
    for i in range(0, 3):
        uppercaseString.append(random.choice(string.ascii_uppercase))
    pw_ucString = map(str, uppercaseString)
    pw_ucString = ''.join(pw_ucString)
    return pw_ucString
def numbers():
    numString = []
    for i in range(0, 2):
        numString.append(random.randint(0, 100))
    pw_numString = map(str, numString)
    pw_numString = ''.join(pw_numString)
    return pw_numString
def symbols():
    symString = []
    for i in range(0, 3):
        symString.append(random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=",
                                        "_", "+", ", ", "<", ">", "/", "?", "[", "]"]))
    pw_symString = map(str, symString)
    pw_symString = ''.join(pw_symString)
    return pw_symString

app = None
window()
passworded()


