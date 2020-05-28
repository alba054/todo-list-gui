from tkinter import ttk, messagebox
import tkinter as tk
from authentication import Login
from module import User
from data_src import UserData, ActivityData
import schedule as sc
import calendar

# global variabel
root = 0
frame1 = 0
frame2 = 0
usernameEntry = 0
passEntry = 0
newUsernameEntry = 0
newPassEntry = 0
user = User()
log = None

def loginbox():
    global root
    global frame1
    global usernameEntry
    global passEntry

    root = tk.Tk()
    root.geometry("300x120")
    root.resizable(width=False, height=False)

    frame1 = tk.Frame(root, padx=15, pady=15)
    usernameEntry = tk.Entry(frame1, width=30)
    passEntry = tk.Entry(frame1, width=30, show="*")

    loginBtn = tk.Button(frame1, text="Login", command=login)
    newAccountBtn = tk.Button(frame1, text="create new account", command=addaccount)

    usernameEntry.pack()
    passEntry.pack()
    loginBtn.pack()
    newAccountBtn.pack()
    frame1.pack()

    root.mainloop()

def login():
    global user
    global log

    log = Login()
    user = log.auth(usernameEntry.get(), passEntry.get())
    if user != None:
        log.checkactivity(user)
        mainapp()

def add():
    userData = UserData()

    if userData.createaccount(newUsernameEntry.get(), newPassEntry.get()):
        frame2.forget()

        frame1.pack()

        messagebox.showinfo("warning", 'Adding new account successfully')
      

def addaccount():
    global newUsernameEntry
    global newPassEntry
    frame1.forget()
    
    frame2 = tk.Frame(root)
    newUsernameEntry = tk.Entry(frame2, width=30)
    newPassEntry = tk.Entry(frame2, width=30, show="*")
    addBtn = tk.Button(frame2, text="add", command=add)
    newUsernameEntry.pack()
    newPassEntry.pack()
    addBtn.pack()
    frame2.pack()

def mainapp():

    frame1.forget()

    frame3 = tk.Frame(root, padx=15, pady=15)
    addBtn = tk.Button(frame3, text='add to do list', command=addtodo)
    deleteBtn = tk.Button(frame3, text='delete', command=delete)
    viewBtn = tk.Button(frame3, text='view to do list', command=view)

    addBtn.grid(row=0, column=0)
    deleteBtn.grid(row=1, column=0)
    viewBtn.grid(row=2, column=0)

    frame3.pack()

def addtodo():

    root2 = tk.Toplevel()

    frame3 = tk.Frame(root2, padx=15, pady=15)
    titlelbl = tk.Label(frame3, text='Judul ')
    timelbl = tk.Label(frame3, text='Jadwal ')
    prioritylbl = tk.Label(frame3, text='Prioritas ')
    desclbl = tk.Label(frame3, text='Deskripsi ')
   

    # form for title
    titleEntry = tk.Entry(frame3, width=40)

    # function for add button
    def callback():
        title = titleEntry.get()
        year = yearComboBox.get()
        month = monthComboBox.get()
        day = dayComboBox.get()
        schedule = f'{year}-{month}-{day}'
        priority = priorityComboBox.get()
        desc = descTextArea.get(1.0, tk.END)
        user.addtodo(title, desc, schedule, priority)
        
        root2.destroy()

        messagebox.showinfo("info", "added to todos")

    addBtn = tk.Button(frame3, text='add todo', command=callback)

    
    def callbackFunc(event):
        year = int(yearComboBox.get())
        monthComboBox.configure(state='readonly', 
                                values=sc.getmonth(year))
        monthComboBox.current(0)

    def callbackFunc1(event):
        year = int(yearComboBox.get())
        month = sc.convertMonthToNum(monthComboBox.get())
        dayComboBox.configure(state='readonly', values=sc.getday(year, month))
        dayComboBox.current(0)

    # form for time

    # year combobox
    yearList = sc.getyear()
    yearComboBox = ttk.Combobox(frame3, values=yearList, state='readonly')

    yearComboBox.current(0)

    yearComboBox.bind("<<ComboboxSelected>>", callbackFunc)

    # month combobox
    monthList = []
    monthComboBox = ttk.Combobox(frame3, values=monthList, state='disabled')
    
    monthComboBox.bind("<<ComboboxSelected>>", callbackFunc1)
    
    # day combobox
    dayList = []
    dayComboBox = ttk.Combobox(frame3, values=dayList, state='disabled')



    # form for priority
    values = ['high', 'normal', 'low']
    priorityComboBox = ttk.Combobox(frame3, values=values, state='readonly')

    # from for description
    descTextArea = tk.Text(frame3, width=30, height=15)

    # focus to this window
    root2.grab_set()

    # get all info every forms

    frame3.pack()
    titlelbl.grid(row=0, column=0)
    timelbl.grid(row=1,column=0)
    prioritylbl.grid(row=2, column=0)
    desclbl.grid(row=3, column=0)
    titleEntry.grid(row=0, column=1, columnspan=3)
    yearComboBox.grid(row=1, column=1)
    monthComboBox.grid(row=1, column=2)
    dayComboBox.grid(row=1, column=3)
    priorityComboBox.grid(row=2, column=1, columnspan=3)
    descTextArea.grid(row=3, column=1, columnspan=3)
    addBtn.grid(row=4, column=1, columnspan=4)


def view():
    log.checkactivity(user)

    root2 = tk.Tk()
    # Using treeview widget 
    treev = ttk.Treeview(root2, selectmode ='browse') 

    # Calling pack method w.r.to treeview 
    treev.pack(side ='top') 

    # Defining number of columns 
    treev["columns"] = ("1", "2", "3", "4",
                        "5", "6", "7") 

    # Defining heading 
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the 
    # respective columns 
    treev.column("1", width = 50, anchor ='c') 
    treev.column("2", width = 100, anchor ='c') 
    treev.column("4", width = 100, anchor ='c') 
    treev.column("5", width = 100, anchor ='c') 
    treev.column("6", width = 100, anchor ='c') 
    treev.column("7", width = 100, anchor ='c') 
    treev.column("3", width = 100, anchor ='c') 

    # Assigning the heading names to the  
    # respective columns 
    treev.heading("1", text ="No") 
    treev.heading("2", text ="Title") 
    treev.heading("3", text ="Status") 
    treev.heading("4", text ="Priority") 
    treev.heading("5", text ="Days Left") 
    treev.heading("6", text ="Schedule") 
    treev.heading("7", text ="Description") 

    # Inserting the items and their features to the  
    # columns built
    i = 1
    for todo in user.activities_list:
        id = todo.id
        title = todo.title
        desc = todo.description
        priority = todo.priority
        time = todo.schedule
        status = "Incomplete" if not todo.status else "Complete"
        days_left = todo.days_left
        treev.insert("", 'end', text =f"L{i}",  
                    values =(id, title, status, priority, days_left, time, desc))
        i += 1

    treev.pack()

def delete():
    log.checkactivity(user)

    root2 = tk.Toplevel()

    def getInfo():
        
        try:
            global root3
            index = int(idEntry.get())
            temp = user.activities_list[index-1]
            root3 = tk.Toplevel()

            frame4 = tk.Frame(root3, padx=15, pady=15)
            frame5 = tk.Frame(root3, padx=15, pady=15)

            idlbl = tk.Label(frame4, text=temp.id)
            titlelbl = tk.Label(frame4, text=temp.title)
            prioritylbl = tk.Label(frame4, text=temp.priority)
            timelbl = tk.Label(frame4, text=temp.schedule)
            statuslbl = tk.Label(frame4, text="Incomplete" if not temp.status else "Complete")
            days_leftlbl = tk.Label(frame4, text=str(temp.days_left) + " day(s) left")
            desclbl = tk.Label(frame4, text=temp.description)

            okBtn = tk.Button(frame5, text="delete", command=confirm)
            noBtn = tk.Button(frame5, text="no", command=root3.destroy)

            idlbl.pack()
            titlelbl.pack()
            prioritylbl.pack()
            timelbl.pack()
            statuslbl.pack()
            days_leftlbl.pack()
            desclbl.pack()

            okBtn.grid(row=0, column=0)
            noBtn.grid(row=0, column=1)

            frame4.pack()
            frame5.pack()

            root3.grab_set()

        except IndexError:
            messagebox.showerror("error", "no id")
        except ValueError:
            messagebox.showerror("error", "input number")

    def confirm():

        user.deltodo(int(idEntry.get()))
        root3.destroy()
        messagebox.showinfo("info", "success")
            


    frame3 = tk.Frame(root2, padx=15, pady=15)
    infolbl = tk.Label(frame3, text="check table for seeing id, click (view)")
    idlbl = tk.Label(frame3, text="input id ")
    idEntry = tk.Entry(frame3, width=15)
    confirmBtn = tk.Button(frame3, text="confirm", command=getInfo)

    frame3.pack()
    infolbl.grid(row=0, column=0, columnspan=2)
    idlbl.grid(row=1, column=0)
    idEntry.grid(row=1, column=1)
    confirmBtn.grid(row=2, column=0, columnspan=2)

    root2.grab_set()



if __name__ == "__main__":
    loginbox()