import tkinter as tk
from ConnectionAPI import ConnectionApi
from ClassData import Data
import customtkinter as ctk

class Create_Frame(Data):
    def __init__(self, window, data, number_lesson, weekday):
        super().__init__(data, number_lesson, weekday)
        self.frame = ctk.CTkFrame(window ,)
        self.frame.grid(column=weekday, row=number_lesson + 1)
        # Create Label
        self.Label1 = ctk.CTkLabel(self.frame, text=self.nameObj)
        self.Label1.pack()
        self.Label2 = ctk.CTkLabel(self.frame, text=self.nameTeach)
        self.Label2.pack()
class App(ConnectionApi, Data):
    day = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    def __init__(self, window):

        self.wind = window
        self.wind.geometry(f'{250}x{200}')
        self.wind.title('Schedule politech')

        #Creating a Frame
        self.frame = ctk.CTkFrame(master=window, width=200, height=200, corner_radius=10)
        self.frame.pack()

        #Creating image
        # self.canvas = ctk.CTkCanvas(self.frame, height=100, width=370)
        # self.img = tk.PhotoImage(file='Headimage.png')
        # self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        # self.canvas.grid(row = 0, column=0)

        #Creating Entry
        self.entry = ctk.CTkEntry(self.frame, width=250)
        self.entry.grid(pady = 50, row = 1, column=0, sticky='n')

        #Creating Button
        self.button = ctk.CTkButton(self.frame,width= 250, text='Найти группу', command=self.get_schedule)
        self.button.grid(pady = 20, row=2, column=0, sticky='s')



    def get_schedule(self):
        
        #Connection API
        group_name = self.entry.get()
        if group_name == '':
            self.button.configure(text= 'Не введена группа')

        else:
            connect = ConnectionApi(group_name)
            self.data_json = connect.schedule_dict
            #Creating Window
            self.schedule = ctk.CTkToplevel()
            self.schedule.title = 'Schedule'
            # Creating Label Frame
            frame = ctk.CTkFrame(self.schedule)
            frame.grid(column=0, row= 0)
            # Creating label
            for i in range(6):
                ctk.CTkLabel(frame, text= App.day[i]).grid(row=0, column=i)
            # Creating Table
            self.create_frame(self.schedule)


    def create_frame(self, window):
        for weekday in range(6):
            for time in range(6):
                try:
                    Create_Frame(window, self.data_json, time, weekday)
                except IndexError:
                    break

