import tkinter as tk
contex = None
from ConnectionAPI import ConnectionApi

date = []

class FrameSchedule(tk.Frame, ConnectionApi):
    def __init__(self, master, a, b):
        super().__init__(master)
        self.grid(column=a, row=b)
        self.label_subject = self.


connect = ConnectionApi()



def button_clicked():
    global context
    context = entrythingy.get()
    connect.get_group_id_by_name(context)
    connect.get_schedule_by_id()
    master.quit()


root = tk.Tk()
master = tk.Frame(root, relief=tk.GROOVE)
master.pack()
canvas = tk.Canvas(master, height=100, width=370)
img = tk.PhotoImage(file='Headimage.png')
image = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.pack()
labelhead = tk.Label(master, text="Введите номер группы")
labelhead.pack()
entrythingy = tk.Entry(master)
entrythingy.pack()
button = tk.Button(master, text='Поиск расписания', command=button_clicked)
button.pack()
root.mainloop()
cshedule = tk.Tk()
frame = tk.Frame(cshedule)
frame.pack()
monday_label = tk.Label(frame, text="Понедельник")
tuesday_label = tk.Label(frame, text="Вторник")
wednesday_label = tk.Label(frame, text="Среда")
thueday_label = tk.Label(frame, text="Четверг")
friday_label = tk.Label(frame, text="Пятница")
saturday_label = tk.Label(frame, text="Суббота")
monday_label.grid(column=0, row=0)
tuesday_label.grid(column=1, row=0)
wednesday_label.grid(column=2, row=0)
thueday_label.grid(column=3, row=0)
friday_label.grid(column=4, row=0)
saturday_label.grid(column=5, row=0)


cshedule.mainloop()

