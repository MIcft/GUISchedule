import tkinter as tk
from ConnectionAPI import *


class App(tk.Frame, ConnectionApi):
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
        self.quit()


class ScheduleFrame(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.monday_label = tk.Label(text="Понедельник")
        self.tuesday_label = tk.Label(text="Вторник")
        self.wednesday_label = tk.Label(text="Среда")
        self.thueday_label = tk.Label(text="Четверг")
        self.friday_label = tk.Label(text="Пятница")
        self.saturday_label = tk.Label(text="Суббота")
        self.monday_label.grid(column=0, row=1)
        self.tuesday_label.grid(column=1, row=1)
        self.wednesday_label.grid(column=2, row=1)
        self.thueday_label.grid(column=3, row=1)
        self.friday_label.grid(column=4, row=1)
        self.saturday_label.grid(column=5, row=1)


#
#
#
#     def create_Head_schedule(self):
#
#         pass



