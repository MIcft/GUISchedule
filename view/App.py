import tkinter as tk
from tkinter import ttk
from ConnectionAPI import ConnectionApi
from ClassData import Data


class Create_Frame(Data):
    def __init__(self, window, data, number_lesson, weekday):
        super().__init__(data, number_lesson, weekday)
        self.frame = tk.Frame(window)
        self.frame.grid(column=weekday, row=number_lesson + 1)
        # Create Label
        self.Label1 = tk.Label(self.frame, text=self.nameObj)
        self.Label2 = tk.Label(self.frame, text=self.nameTeach)
class App(ConnectionApi, Data):
    day = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    def __init__(self, window):

        self.wind = self.wind = window
        self.wind.title('Schedule politech')

        #Creating a Frame
        self.frame = tk.Frame(self.wind)
        self.frame.grid(row = 0, column=0)

        #Creating image
        self.canvas = tk.Canvas(self.frame, height=100, width=370)
        self.img = tk.PhotoImage(file='Headimage.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.grid(row = 0, column=0)

        #Creating Entry
        self.entry = tk.Entry(self.frame, width=60)
        self.entry.grid(row = 1, column=0)

        #Creating Button
        self.button = tk.Button(self.frame, text='Найти группу', command=self.get_schedule)
        self.button.grid(row=2, column=0)



    def get_schedule(self):
        #Connection API
        group_name = self.entry.get()
        connect = ConnectionApi(group_name)
        self.data_json = connect.schedule_dict
        #Creating Window
        self.schedule = tk.Toplevel()
        self.schedule.title = 'Schedule'
        # Creating Label Frame
        frame = tk.Frame(self.schedule)
        frame.grid(column=0, row= 0)
        # Creating label
        for i in range(6):
            tk.Label(frame, text= App.day[i]).grid(row=0, column=i)
        # Creating Table
        self.create_frame(self.schedule)

        # Table
        # columns = ("#1", "#2", "#3", "#4", "#5")
        # self.tree = ttk.Treeview(self.schedule, height=10, columns=columns)
        # self.tree.grid(row=4, column=0, columnspan=6)
        # self.tree.heading('#0', text='Понедельник', anchor=tk.CENTER)
        # self.tree.heading('#1', text='Вторник', anchor=tk.CENTER)
        # self.tree.heading('#2', text='Среда', anchor=tk.CENTER)
        # self.tree.heading('#3', text='Четверг', anchor=tk.CENTER)
        # self.tree.heading('#4', text='Пятница', anchor=tk.CENTER)
        # self.tree.heading('#5', text='Суббота', anchor=tk.CENTER)

    def create_frame(self, window):
        for weekday in range(6):
            for time in range(6):
                Create_Frame(window, self.data_json, time, weekday)













if __name__ == '__main__':
    window = tk.Tk()
    application = App(window)
    window.mainloop()