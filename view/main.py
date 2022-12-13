from AuthorizationApp import  *
from ConnectionAPI import *
if __name__ == '__main__':
    root = tk.Tk()
    myapp = AuthorizationApp(root)
    schedule = ScheduleFrame(root, myapp)
    root.mainloop()
