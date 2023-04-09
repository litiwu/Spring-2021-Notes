# lisa wu LXW190014 
# CS 4348.003 Project 2 

import threading
import random

gLock = threading.Semaphore(1)
gCount = 0

# door semaphore - two threads can enter at one time
doorSemaphore = threading.Semaphore(2)

# initiate the tables, each can take 4 customers - can only have 4 threads at a table at a time
tableASemaphore = threading.Semaphore(4)
tableBSemaphore = threading.Semaphore(4)
tableCSemaphore = threading.Semaphore(4)
tables = [tableASemaphore, tableBSemaphore, tableCSemaphore]
tableFoods = ["A", "B", "C"]

tableLines = [0,0,0]


# order semaphores for each table for the waiters - signals when order can be take
waiter0Semaphore = threading.Semaphore(0)
waiter1Semaphore = threading.Semaphore(0)
waiter3Semaphore = threading.Semaphore(0)

# kitchen semaphore - one waiter in there at a time
kitchenSemaphore = threading.Semaphore(0)

restaurant = 0

def threadcode(id):
    global gCount
    gLock.acquire()
    print("Thread " + str(id) + " has count " + str(gCount))
    gCount = gCount+1
    gLock.release()

def enterRestaurant(id):
    doorSemaphore.acquire()
    print("Customer " + str(id) + " enters restaurant")
    doorSemaphore.release()

    # customer picks what they want to eat
    customerChoice = random.randint(0,2)
    customerBackup = customerChoice 

    print(f"Customer {id} wants to eat {tableFoods[customerChoice]}")

    if(random.randint(0,1) == 1):
        while(customerBackup == customerChoice):
            customerBackup = random.randint(0,2)
            print(f"Customer {id}'s backup choice is {tableFoods[customerChoice]}")

    
    
    if (customerBackup == customerChoice or tableLines[customerChoice] < 7):
        if(tables[customerChoice])
        tables[customerChoice].acquire()
        print(f"Customer {id} sits at table {customerChoice}")
    else: 
        tables[customerBackup].acquire()
        


def createWaiters(id, table):
    # they go to the table and are ready to take orders
    table.acquire()

    if id == 0:
        print ("Waiter " + str(id) + " is assigned to Table A")
    elif id == 1:
        print ("Waiter " + str(id) + " is assigned to Table B")
    elif id == 2:
        print ("Waiter " + str(id) + " is assigned to Table C")

    



    
# initialize the waiters 
for wid in range (0,3):
    t = threading.Thread (target=createWaiters, args=(wid, tables[wid]))
    t.start()
    


for cid in range(0,40):
    t = threading.Thread(target=enterRestaurant,args=(cid,))
    # starts the function that the thread will run
    t.start()
