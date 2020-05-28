import schedule as sc

class User:

    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password
        self.activities_list = []
    
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