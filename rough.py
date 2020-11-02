createButton = Button(window, text="Create Textfile", font=("Arial", 12, "bold"), relief=RAISED, bd=5,
                       justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue", command=create_file)
createButton.grid(row=6, column=0)

displayButton = Button(window, text="Display", font=("Arial", 12, "bold"), relief=RAISED, bd=5,
                       justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue")
displayButton.grid(row=6, column=1)

appendButton = Button(window, text="Append Data", font=("Arial", 12, "bold"), relief=RAISED, bd=5,
                       justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue")
appendButton.grid(row=6, column=2)

clearButton = Button(window, text="Clear", font=("Arial", 12, "bold"), relief=RAISED, bd=5,
                       justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue")
clearButton.grid(row=6, column=3)

exitButton = Button(window, text="Exit", font=("Arial", 12, "bold"), relief=RAISED, bd=5,
                       justify=CENTER,
                       highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue", command=window.quit)
exitButton.grid(row=6, column=4)


titlelabel = Label(window, text="My Weekend Activities", font=("Arial", 20, "bold", "underline"),
                   justify=CENTER, background="purple")
titlelabel.grid(row=1, column=2)

first_entry = Text(window, width = 40, height = 5)
first_entry.grid(row=2, column=2, columnspan=4, padx=12, ipady=14, rowspan=4)

btn_create = Button(window, text="Create Textfile", command=create_file).place(x=10, y=150)
mybutton = Button(window, text="Display", command=text_file).place(x=150, y=150)
mybutton1 = Button(window, text="Append Data").place(x=230, y=150)
mybutton2 = Button(window, text="Clear").place(x=350, y=150)
mybutton3 = Button(window, text="Exit").place(x=420, y=150)