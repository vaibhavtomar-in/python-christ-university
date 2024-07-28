def tempAbove30(list1):
    count=0
    for i in list1:
        if (i["max_temp"]>30):
            count+=1
    return count

def avgHumidity(list1, startDate, days):
    humidity = 0
    index = 0
    for i in range(len(list1)):
        if (list1[i]["date"] == startDate):
            index = i
    for i in list1[index:index+days]:
        humidity+=i["humidity"]
    return humidity/days

def highLowWeek(list1, startDate):
    highTemp= -999
    lowTemp = 999
    index = 0
    for i in range(len(list1)):
        if (list1[i]["date"] == startDate):
            index = i
    for i in list1[index:index+7]:
        if (i["max_temp"]> highTemp):
            highTemp = i["max_temp"]
        if (i["min_temp"] < lowTemp):
            lowTemp = i["min_temp"]
    return [highTemp, lowTemp]
