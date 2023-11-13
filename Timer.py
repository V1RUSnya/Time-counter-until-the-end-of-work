# -*- coding: cp1251 -*-
import datetime
import os

def zerozero(number):
    n = str(number)
    if len(n) == 1:
        n = "0"+n
    return n

def difference(actual_time):
    all_wait_time = 16*3600 + 30*60
    difference_time = int(actual_time[0:2])*3600 + int(actual_time[3:5])*60
    dif = all_wait_time - difference_time
    dif = dif/60
    hours = dif // 60
    minutes = dif % 60
    if int(hours) > 0 and int(hours) < 5:
        hour = "часа"
    else:
        hour = "часов"
    os.system('cls')
    print(f"Время: {actual_time}\nОсталось работать: {int(hours)} {hour} и {int(minutes)} минут")

def timer(memory):
    time = datetime.datetime.now()
    if time.second != memory:
        memory = time.second
        output = zerozero(time.hour) + ":" + zerozero(time.minute) + ":" + zerozero(memory)
        difference(output)
    return memory 


    

memory = datetime.datetime.now()
memory = memory.second
while True:
    memory = timer(memory)
