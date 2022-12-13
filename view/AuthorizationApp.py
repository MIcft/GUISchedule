import tkinter as tk
from ConnectionAPI import *


class AuthorizationApp(tk.Frame, ConnectionApi):
    """
    Класс для создания окна авторизации
    """

    def __init__(self, master):
        super().__init__(master)
        self.connect = None
        self.context = None
        self.isbutton_clicked = False
        self.canvas = tk.Canvas(master, height=100, width=370)
        self.img = tk.PhotoImage(file='Headimage.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.pack()
        self.labelhead = tk.Label(text="Введите номер группы")
        self.labelhead.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.button = tk.Button(text='Поиск расписания', command=self.button_clicked)
        self.button.pack()
        self.pack()

    def button_clicked(self):
        self.isbutton_clicked = True
        self.context = self.entrythingy.get()
        self.get_group_id_by_name(self.context)
        self.get_schedule_by_id()


class ScheduleFrame(tk.Frame):
    def __init__(self, master, app):
        self.label1 = None
        self.app = app
        if self.app.isbutton_clicked:
            super().__init__(master)
            self.create_Head_schedule()
            self.app.quit()


    def create_Head_schedule(self):
        self.label1 = tk.Label(text="Привет андрей")
        pass



