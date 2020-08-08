# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# myao,08.04.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = "C:\_PythonClass\Module 05\ToDoList.txt"
strData = open(objFile, "r")
for row in strData:
    lstTable = row.split(',')
    dicRow = {lstTable[0]: lstTable[1].strip()}
strData.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        print("Task and Priority")
        objFile = "C:\_PythonClass\Module 05\ToDoList.txt"
        strData = open(objFile, "r")
        for row in strData:
            lstTable = row.split(',')
            dicRow = {lstTable[0]: lstTable[1].strip()}
            print(dicRow)
        strData.close()
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("type in 'Task' and Priority")
        newdata1 = input("Enter a Task: ")
        newdata2 = input("Enter a priority: ")
        dicRow = {newdata1: newdata2.strip()}
        print(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        objFile = "C:\_PythonClass\Module 05\ToDoList.txt"
        strData = open(objFile, "r")
        dicRow = {row.split(",")[0]: row.split(",")[1].strip() for row in strData}
        print("Task and Priority\n", dicRow)
        delete_item = input("What item do you want me to remove?: ")
        if delete_item in dicRow:
            del dicRow[delete_item]
            print("\nOkay, I removed", delete_item)
            print("Current data is\n ", dicRow)
        else:
            print( delete_item, "doesn't exist in the list.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = "C:\_PythonClass\Module 05\ToDoList.txt"
        strData = open(objFile, "a")
        strData.write(newdata1 + ',' + newdata2 + '\n')
        strData.close()
        print('Save to File')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exit Program")
        break  # and Exit the program
