from tkinter import *

window = Tk()
window.title("Text Files")
window.geometry("700x700")
window.configure(background="purple")

def create_file():
    file = open('/home/user/Desktop/MondayWork.txt', 'w')
    file.write("Hey Nadine - Whatsapp\n")
    file.write("What are you doing over the weekend?")
    file.close()

def text_file():
    file = open('/home/user/Desktop/MondayWork.txt', 'r')
    for each in file:
        TEXT.insert(END, each)
    file.close()

def append():
    file = open('/home/user/Desktop/MondayWork.txt', 'a')
    file.writelines(TEXT.get("1.0", "end-1c")+"\n")

num1_label = Label(window, text="My Weekend Activities")
num1_label.grid(row=0, column=1)

TEXT = Text(window, height = 5, width = 40)
TEXT.grid(row = 3, column = 1, columnspan = 3, pady = 10, padx = 20)


create = Button(window, text = "CREATE TEXTFILE",font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green",activeforeground="blue", command=create_file)
create.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 20)

DISPLAY = Button(window, text = "DISPLAY",font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green",activeforeground="blue", command=text_file)
DISPLAY.grid(row = 5, column = 2, columnspan = 3, pady = 10, padx = 20)

APPEND = Button(window, text = "APPEND DATA", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green", activeforeground="blue", command=append)
APPEND.grid(row = 5, column = 4, columnspan = 3, pady = 10, padx = 20)




EXIT = Button(window, text = "Exit", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE,activebackground = "green",activeforeground="blue",command = window.destroy)
EXIT.grid(row = 5, column = 10, columnspan = 3, pady = 10, padx = 20)

def clear():
    TEXT.delete('1.0', 'end')

clearButton = Button (window, text = "Clear", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = clear)
clearButton.grid(row = 5, column = 7,ipady = 8, ipadx = 12, pady = 5, sticky = NW)












window.mainloop()