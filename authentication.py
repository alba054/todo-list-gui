from data_src import ActivityData, UserData
from module import User, Activity
from tkinter import messagebox
import json

class Login:

    def __init__(self):
        self.user = User()
        self.userData = UserData()
        self.activityData = ActivityData()

    def auth(self, username, password):
        if username in self.userData.map_user.keys():
            if password == self.userData.map_user[username][0]:
                id = self.userData.map_user[username][-1]
                self.user = User(id, username, password)

                return self.user

            else:
                messagebox.showerror('error', "wrong password")
        else:
            messagebox.showerror('error',"no account")

    def checkactivity(self, user):
        json_parsed = self.activityData.readfile()
        raw_activity_ls = json_parsed[str(user.id)]
        user.activities_list = []
        for values in raw_activity_ls:
                title = values["title"]
                desc = values["description"]
                priority = values["priority"]
                schedule = values["schedule"]
                id = values["id"]
                activity = Activity(title, desc, priority, schedule, id)
                activity.days_left = activity.setDaysLeft()
                activity.status = activity.checkstatus()
                user.activities_list.append(activity)
                