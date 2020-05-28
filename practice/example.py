# # # import tkinter as tk
# # # from tkinter import ttk

# # # from tkinter import *

# # # m=Tk()
# # # m.title("Parent")
# # # c=Toplevel(m)
# # # c.title("Child")
# # # Button(c,text="Hello",command=c.destroy).pack()

# # # c.bind("<Destroy>",lambda x:m.deiconify())
# # # # note we need lambda to get rid of the Destroy argument
# # # #we should "bind", because there are many ways a window can be killed

# # # m.withdraw()

# # # mainloop()

# # # def callbackFunc(event):
# # #      print("New Element Selected")
     
# # # app = tk.Tk() 
# # # app.geometry('200x100')

# # # labelTop = tk.Label(app,
# # #                     text = "Choose your favourite month")
# # # labelTop.grid(column=0, row=0)

# # # comboExample = ttk.Combobox(app, 
# # #                             values=[
# # #                                     "January", 
# # #                                     "February",
# # #                                     "March",
# # #                                     "April"], state='readonly')


# # # comboExample.grid(column=0, row=1)
# # # comboExample.current(0)

# # # comboExample.bind("<<ComboboxSelected>>", callbackFunc)


# # # app.mainloop()

# # # import tkinter as tk
# # # from tkinter import ttk

# # # def callbackFunc(event):
# # #      print("New Element Selected")
     
# # # # app = tk.Tk() 
# # # # app.geometry('200x100')

# # # # def changeMonth():
# # # #     comboExample["values"] = ["July",
# # # #                               "August",
# # # #                               "September",
# # # #                               "October"
# # # #                                 ]

# # # # labelTop = tk.Label(app,
# # # #                     text = "Choose your favourite month")
# # # # labelTop.grid(column=0, row=0)

# # # # comboExample = ttk.Combobox(app, 
# # # #                             values=[
# # # #                                     "January", 
# # # #                                     "February",
# # # #                                     "March",
# # # #                                     "April"],
# # # #                             postcommand=changeMonth)


# # # # comboExample.grid(column=0, row=1)

# # # # app.mainloop()


# # from tkinter import *


# # class GUI(Frame):


# #     def __init__(self, master, *args, **kwargs):
# #         Frame.__init__(self, master, *args, **kwargs)

# #         self.master = master
# #         self.my_frame = Frame(self.master)
# #         self.my_frame.pack()

# #         self.button1 = Button(self.master, text="Open New Window", command = self.open_toplevel_window)
# #         self.button1.pack()

# #         self.text = Text(self.master, width = 20, height = 3)
# #         self.text.pack()
# #         self.text.insert(END, "Before\ntop window\ninteraction")

# #     def open_toplevel_window(self):
# #         self.top = Toplevel(self.master)
# #         #this forces all focus on the top level until Toplevel is closed
# #         self.top.grab_set() 

# #         def replace_text():
# #             self.text.delete(1.0, END)
# #             self.text.insert(END, "Text From\nToplevel")

# #         top_button = Button(self.top, text = "Replace text in main window",
# #                             command = replace_text)
# #         top_button.pack()


# # if __name__ == "__main__":
# #     root = Tk()
# #     app = GUI(root)
# #     root.mainloop()


# Python program to illustrate the usage of  
# treeview scrollbars using tkinter 
  
  
from tkinter import ttk 
import tkinter as tk 
  
# Creating tkinter window 
window = tk.Tk() 
window.resizable(width = 1, height = 1) 
  
# Using treeview widget 
treev = ttk.Treeview(window, selectmode ='browse') 
  
# Calling pack method w.r.to treeview 
treev.pack(side ='right') 
  
# Constructing vertical scrollbar 
# with treeview 
# verscrlbar = ttk.Scrollbar(window,  
#                            orient ="vertical",  
#                            command = treev.yview) 
  
# Calling pack method w.r.to verical  
# scrollbar 
# verscrlbar.pack(side ='right', fill ='x') 
  
# # Configuring treeview 
# treev.configure(xscrollcommand = verscrlbar.set) 
  
# Defining number of columns 
treev["columns"] = ("1", "2", "3") 
  
# Defining heading 
treev['show'] = 'headings'
  
# Assigning the width and anchor to  the 
# respective columns 
treev.column("1", width = 90, anchor ='c') 
treev.column("2", width = 90, anchor ='se') 
treev.column("3", width = 90, anchor ='se') 
  
# Assigning the heading names to the  
# respective columns 
treev.heading("1", text ="Name") 
treev.heading("2", text ="Sex") 
treev.heading("3", text ="Age") 
  
# Inserting the items and their features to the  
# columns built 
treev.insert("", 'end', text ="L1",  
             values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2", 
             values =("Nisha", "F", "23")) 
treev.insert("", 'end', text ="L3", 
             values =("Preeti", "F", "27")) 
treev.insert("", 'end', text ="L4", 
             values =("Rahul", "M", "20")) 
treev.insert("", 'end', text ="L5",  
             values =("Sonu", "F", "18")) 
treev.insert("", 'end', text ="L6", 
             values =("Rohit", "M", "19")) 
treev.insert("", 'end', text ="L7",  
             values =("Geeta", "F", "25")) 
treev.insert("", 'end', text ="L8",  
             values =("Ankit", "M", "22")) 
treev.insert("", 'end', text ="L10",  
             values =("Mukul", "F", "25")) 
treev.insert("", 'end', text ="L11", 
             values =("Mohit", "M", "16")) 
treev.insert("", 'end', text ="L12", 
             values =("Vivek", "M", "22")) 
treev.insert("", 'end', text ="L13", 
             values =("Suman", "F", "30")) 
  
# Calling mainloop 
window.mainloop()

# import tkinter as tk
# from tkinter import ttk

# class App:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.tree = ttk.Treeview()
#         self.tree.pack()
#         for i in range(10):
#             self.tree.insert("", "end", text="Item %s" % i)
#         self.tree.bind("<Double-1>", self.OnDoubleClick)
#         self.root.mainloop()

#     def OnDoubleClick(self, event):
#         item = self.tree.selection()[0]
#         print(self.tree.selection)
#         print("you clicked on", self.tree.item(item,"text"))

# if __name__ == "__main__":
#     app = App()