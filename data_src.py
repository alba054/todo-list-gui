import json
from tkinter import messagebox

class UserData:

    def __init__(self, src="./data/user.json"):
        self.file = src
        self.map_user = {}
        self.readfile()

    def readfile(self):
        with open(self.file) as f:
            try:
                json_data = json.load(f)
            except Exception:
                pass
        
        for user in json_data:
            self.map_user[user["username"]] = [user["password"], user["id"]]

    def writefile(self, file, data):
        with open(file, "w") as f:
            json.dump(data, f)

    def checkaccount(self, username):
        with open(self.file) as f:
            json_data = json.load(f)
        
        for account in json_data:
            if account["username"] == username:
                return True
            
        return False

    def createaccount(self, username, password):
        if not self.checkaccount(username):
            with open(self.file) as f:
                json_data = json.load(f)
            
            with open('./data/todo.json') as f:
                todo_json = json.load(f)

            # id == numbers of account in user.json
            id = len(json_data) + 1
            
            # created account is appended to user.json
            data_to_append = {"id":id, "username":username, "password":password}

            # update todo.json
            todo_to_append = {str(id):[]}
            todo_json.update(todo_to_append)
            self.writefile('./data/todo.json', todo_json)

            # append new account to user.json
            json_data.append(data_to_append)

            # rewrite user.json
            self.writefile(self.file, json_data)

            self.__init__()

            return True

        else:
            messagebox.showerror('error', "Username Has Been Used")



from module import User

class ActivityData:
    
    def __init__(self, src="./data/todo.json"):
        self.file = src
        self.readfile()

    def writefile(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f)

    def readfile(self):
        with open(self.file) as f:
            try:
                json_data = json.load(f)
                return json_data
            except Exception:
                pass
        
    def addtodo(self, user, title, desc, schedule, priority):
        with open(self.file) as f:
            json_data = json.load(f)

        temp = json_data[str(user.id)]

        # number of todos
        id = len(temp) + 1

        # new todo is appended to todo.json
        data_to_append = {

            "id":id,
            "title":title,
            "description":desc,
            "priority":priority,
            "schedule":schedule
        }

        temp.append(data_to_append)

        self.writefile(json_data)

        self.__init__()

        return True

    def deltodo(self, user, id_to_remove):
        with open(self.file) as f:
            json_data = json.load(f)

        temp = json_data[str(user.id)]

        i = 0
        for todo in temp:
            if todo["id"] == id_to_remove:
                temp.pop(i)
                break
            
            i += 1

        for i in range(len(temp)):
            temp[i]["id"] = i+1
        
        self.writefile(json_data)

        self.__init__()

        
