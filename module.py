import schedule as sc
from data_src import ActivityData

class User:

    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password
        self.activities_list = []
        self.activityData = ActivityData()

    def addtodo(self, title, desc, schedule, priority):
        json_data = self.activityData.readfile()

        temp = json_data[str(self.id)]

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

        self.activityData.writefile(json_data)

        self.activityData.__init__()

        return True

    def deltodo(self, id_to_remove):
        json_data = self.activityData.readfile()

        temp = json_data[str(self.id)]

        i = 0
        for todo in temp:
            if todo["id"] == id_to_remove:
                temp.pop(i)
                break
            
            i += 1

        for i in range(len(temp)):
            temp[i]["id"] = i+1
        
        self.activityData.writefile(json_data)

    
import datetime


class Activity:

    def __init__(self, title=None, 
                       description=None, 
                       priority=None, 
                       schedule=None, 
                       id=None
                       ):

        self.title = title
        self.description = description
        self.status = None
        self.priority = priority
        self.schedule = schedule
        self.id = id
        self.days_left = None


    def setDaysLeft(self):
        year = self.schedule.split('-')[0]
        month = sc.convertMonthToNum(self.schedule.split('-')[1])
        day = self.schedule.split('-')[2]
        days_left = datetime.date(int(year), int(month), int(day)) - datetime.date.today()

        return days_left.days

    def checkstatus(self):

        return False if self.setDaysLeft() > 0 else True