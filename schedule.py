import datetime
import calendar

today = datetime.date.today()

def getyear():
    yearList = []

    for i in range(10):
        yearList.append(today.year + i)
    
    return yearList


def getmonth(selectedYear):
    monthList = []

    if selectedYear > today.year:
        for i in range(1, 13):
            monthList.append(calendar.month_name[i])
    
    else:
        for i in range(today.month, 13):
            monthList.append(calendar.month_name[i])

    return monthList

def getday(selectedYear, selectedMonth):

    if selectedYear > today.year:
        numberOfDaysInCurMonth = calendar.monthrange(selectedYear, selectedMonth)[1]

        dayList = [day for day in range(1, numberOfDaysInCurMonth+1)]

    else:
        if selectedMonth > today.month:
            numberOfDaysInCurMonth = calendar.monthrange(selectedYear, selectedMonth)[1]

            dayList = [day for day in range(1, numberOfDaysInCurMonth+1)]
        else:
            numberOfDaysInCurMonth = calendar.monthrange(selectedYear, selectedMonth)[1]

            dayList = [day for day in range(today.day, numberOfDaysInCurMonth+1)]

    return dayList


def convertMonthToNum(month_name):
    map = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12
    }

    return map[month_name]
