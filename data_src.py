import json
from tkinter import messagebox

class DataSource:

    def __init__(self, src):
        self.file = src

    def readfile(self):
        with open(self.file) as f:
            try:
                json_data = json.load(f)
                return json_data
            except Exception:
                pass

    def writefile(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f)


class UserData(DataSource):

    def __init__(self, src="./data/user.json"):
        super().__init__(src)
        self.map_user = {}
        self.readfile()

    def readfile(self):
        json_data = super().readfile()
        
        for user in json_data:
            self.map_user[user["username"]] = [user["password"], user["id"]]


    def checkaccount(self, username):
        json_data = super().readfile()
        
        for account in json_data:
            if account["username"] == username:
                return True
            
        return False

    def createaccount(self, username, password):
        if not self.checkaccount(username):
            json_data = super().readfile()
            
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




class ActivityData(DataSource):
    
    def __init__(self, src="./data/todo.json"):
        super().__init__(src)
        self.readfile()

        
