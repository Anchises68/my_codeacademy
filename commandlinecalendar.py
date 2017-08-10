#command line  calendar
from time import sleep, strftime
from datetime import datetime

USER_NAME = "Julio"

calendar  = {}

def welcome():
    print ("Hello, " + USER_NAME)
    print ("Open Calendar")
    sleep(1)
    print ("Today is " + strftime("%A %B %d, %Y"))
    sleep(1)
    print (strftime("%H:%M:%S"))
    sleep(1)
    print ("What would you like to do?")
    
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input('A to Add, U to Update, V to View, D to Delete, X to Exit: ')
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print ("Calendar Empty")
            else:
                print (calendar)
        elif user_choice == "U":
            date = str(raw_input("What date? "))
            try:
                date = datetime.strptime(date, '%Y, %m, %d')
            except ValueError:
                print ("FORMAT ERROR!")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print ("Shit's updated")
            print (calendar)
        elif user_choice == "A":
            event = raw_input("Enter event: ")
            date = str(raw_input("Enter date: Year, month, day: "))
            try:               
                date =  datetime.strptime(date, '%Y, %m, %d')                                           
            except ValueError:
                print ("Format Error")
            calendar[date] = event
            print (calendar)
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print ("Empty Date!")
            else:
                event = raw_input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print ("Event was deleted.")
                        sleep(1)
                        print (calendar)
                    else:
                        print ("Event not found")
        elif user_choice == "X":
            start = False
        else:
            print ("Wrong Input. Terminating!")
            start = False
                   
start_calendar()       