import tkinter as tk

class AuthorizationApp(tk.Frame):
    """
    Класс для создания окна авторизации
    """
    def __init__(self, master):
        super().__init__(master)
        self.canvas = tk.Canvas(master, height=100, width=370)
        self.img = tk.PhotoImage(file='Headimage.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.pack()
        self.pack()
        self.labelhead = tk.Label(text="Введите номер группы")
        self.labelhead.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.button = tk.Button(text='Поиск расписания')
        self.button.pack()


        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("3332201/90101")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.return_contents)


    def return_contents(self, event):
        return self.contents.get()
