from App import  *
from ConnectionAPI import *
if __name__ == '__main__':
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()
    schedule = ScheduleFrame(root, myapp)
    schedule.mainloop()
