# Import modules
import tkinter
import datetime


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        # Define widgets
        self.label = tkinter.Label(self, text="How many years old are you?")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.getage)
        # Pack widgets again
        self.label.pack()
        self.entry.pack()
        self.button.pack()
    # Function to get user's age
    def getage(self):
        global age
        global iage
        age = self.entry.get()
        iage = int(age)
        # Erase widgets
        self.label.forget()
        self.entry.forget()
        self.button.forget()
        # Define widgets again
        self.label = tkinter.Label(self, text="At what hour would you like to wake?")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.getwake)
        # Pack widgets again
        self.label.pack()
        self.entry.pack()
        self.button.pack()
    # Get hour user wants to wake
    def getwake(self):
        global wake
        global iwake
        wake = self.entry.get()
        iwake = int(wake)
        # Erase widgets again
        self.label.forget()
        self.entry.forget()
        self.button.forget()
        # Define widgets again
        self.label = tkinter.Label(self, text="How many hours ago did you last eat?")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.getlmeal)
        # Pack widgets again
        self.label.pack()
        self.entry.pack()
        self.button.pack()
    def getlmeal(self):
        global lmeal
        global ilmeal
        lmeal = self.entry.get()
        ilmeal = int(lmeal)
        # Erase widgets again
        self.label.forget()
        self.entry.forget()
        self.button.forget()
        # Define widgets again
        self.label = tkinter.Label(self, text="How many hours ago did you last\nuse an electronic device?")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.getlusage)
        # Pack widgets again
        self.label.pack()
        self.entry.pack()
        self.button.pack()
    def getlusage(self):
        global lusage
        global ilusage
        lusage = self.entry.get()
        ilusage = int(lusage)
        # Erase widgets again
        self.label.forget()
        self.entry.forget()
        self.button.forget()
        # Define widgets again
        self.label = tkinter.Label(self, text="How many hours ago did you last exercise?")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.getlexer)
        # Pack widgets again
        self.label.pack()
        self.entry.pack()
        self.button.pack()
    def getlexer(self):
        global wait
        wait = 0
        global lexer
        global ilexer
        lexer = self.entry.get()
        ilexer = int(lexer)
        # Erase widgets again
        self.label.forget()
        self.entry.forget()
        self.button.forget()
        if iage < 8:
            sleep = 12
            if ilexer <= 1 and ilmeal <= 2:
                sleep = sleep + 2
            elif ilexer <= 1 and ilmeal < 2:
                sleep = sleep + 1
            elif ilexer > 1 and ilmeal <= 2:
                sleep = sleep + 2
            else:
                print("")

        elif iage >= 8 and iage < 12:
            sleep = 10
            if ilexer <= 1 and ilmeal <= 2:
                sleep = sleep + 2
            elif ilexer <= 1 and ilmeal < 2:
                sleep = sleep + 1
            elif ilexer > 1 and ilmeal <= 2:
                sleep = sleep + 2
            else:
                print("")

        elif iage >= 12 and iage < 17:
            sleep = 9
            if ilexer <= 1 and ilmeal <= 2:
                sleep = sleep + 2
            elif ilexer <= 1 and ilmeal < 2:
                sleep = sleep + 1
            elif ilexer > 1 and ilmeal <= 2:
                sleep = sleep + 2
            else:
                print("")

        elif iage >= 18:
            sleep = 8
            if ilexer <= 1 and ilmeal <= 2:
                sleep = sleep + 2
            elif ilexer <= 1 and ilmeal < 2:
                sleep = sleep + 1
            elif ilexer > 1 and ilmeal <= 2:
                sleep = sleep + 2
            else:
                print("")

        sleeptime = int(datetime.timedelta(hours = iwake - sleep).seconds / 3600)


        # Create widgets again
        self.label = tkinter.Label(text="{} hours of sleep is optimal for you.".format(sleep), font="Helvetica 18 bold")
        self.label2 = tkinter.Label(text="You should go to bed at {} hours to wake up at\n{} hours with optimal sleep.".format(sleeptime, iwake), font="Helvetica 11 bold")
        # Pack widgets again
        self.label.pack(pady=10)
        self.label2.pack()


# Draw window
window = App()
window.title("Sleep Calculator")
window.geometry("500x250")
window.mainloop()
