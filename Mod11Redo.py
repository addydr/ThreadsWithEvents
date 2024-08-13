"""
Name:Addison deAbreu-Reese
Date:11/11/2023
Assignment: Module 11: Using Threads with Events
Due Date:11/12/2023
About this project: This project implements threads with events
Assumptions:NA
All work below was performed by Addison deAbreu-Reese and Karen Works, PhD.
"""
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import random
import time
import threading
# Function Name:task()
# Definition:   Calculates future value FV = PV * [ 1 + ( i / n ) ] ^ (n * t)
# Parameters:   PV = Present Value, i = interest rate period, n = no. of compounding periods per year,
#               t = number of years. e for event
timelist = []
vallist = []

def task(PV, i, n, t, e):
    global timelist
    global vallist

    FV = PV * (1 + (i / n)) ** (n * t)  # Calculate and return Future Value

    timelist.append(t)                  #append FV and t to respective lists
    vallist.append(FV)
    e.set()                             #set event

def disp(events):
    global timelist
    global vallist
    #print("Test3")

    while not all([e.is_set() for e in events]):    #while events are not all complete, wait
        #print("test4")
        for e in events:
            #print("test5")
            e.wait(1)
    print("Total number of payments: ", timelist[0], " Future Value: ", vallist[0])
    print("Total number of payments: ", timelist[1], " Future Value: ", vallist[1])
    print("Total number of payments: ", timelist[2], " Future Value: ", vallist[2])

    indMax = 0                              #finds highest value on vallist
    for i in range(1, len(vallist)):
        if vallist[indMax] < vallist[i]:
            indMax = i

    print("Highest Future Value: ")
    if (indMax == 0):
        print(vallist[0])
    elif (indMax == 1):
        print(vallist[1])
    elif (indMax == 2):
        print(vallist[2])

if __name__ == '__main__':
    PV = 20000                          # Preset a initial Present Value
    n = 4                               # Preset the total number of compounding periods per year
    random.seed(time.time())            #Create three random values between 5 % and 10% for the interest rate
    r1 = random.uniform(.05,.1)
    r2 = random.uniform(.05,.1)
    r3 = random.uniform(.05,.1)

    e1 = threading.Event()              #events
    e2 = threading.Event()
    e3 = threading.Event()
    events = [e1, e2, e3]               #events list
    #print("Test1")
    #function calls with events
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(task, PV, r1, n, 10, e1)
        executor.submit(task, PV, r2, n, 20, e2)
        executor.submit(task, PV, r3, n, 30, e3)
        executor.submit(disp, events)

    #print("Test2")

    #disp(events)
