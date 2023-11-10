# -*- coding: cp1251 -*-
import datetime
import os

def zerozero(number):
    n = str(number)
    if len(n) == 1:
        n = "0"+n
    return n

def difference(actual_time):
    wait_time_hour = 16
    wait_time_minute = 30
    difference_hour = int(actual_time[0:2])
    difference_minute = int(actual_time[3:5])
    wait_second = 60 - int(actual_time[6:8])
    os.system('cls')
    if int(actual_time[3:5])>30:
        wait_minute = 60 - int(actual_time[3:5])
    else:
        wait_minute = wait_time_minute - int(actual_time[3:5])
    if int(wait_time_hour - difference_hour) > 0 and int(wait_time_hour - difference_hour) < 5:
        hour = "часа"
    else:
        hour = "часов"
        
    print(f"Время: {actual_time}\nОсталось работать: {wait_time_hour - difference_hour} {hour}, {wait_minute} минут и {wait_second} секунд")

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
