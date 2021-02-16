# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Hannah Clayton,12Feb21, Added code to initialize assignment 5
# Hannah Clayton, 13Feb21, Broke down each segment into different files
#                          for easier comprehension, input code for steps
#                          1-5
# Hannah Clayton, 14 Feb 21, Resolved error 'index value out of range' that
#                           that was caused by incorrect typing in processing
#                           section, finished code.
# ------------------------------------------------------------------------ #
# -- Data --#
txtFile = "ToDoList.txt"  # An object that represents a file
txtData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table = []  # A list that acts as a 'table' of rows
userMenu = ""  # A menu of user options
userChoice = ""  # A Capture the user option selection

# -- Processing -- #
# load data from text file when starting
txtFile = open('C:/02_pythonclass/Assignment05/ToDoList.txt', 'r')
for row in txtFile:
    lstRow = row.split(" | ")
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}  # .strip() removes the visible '\n' when printing
    table.append(dicRow)
txtFile.close()

# # # -- Input/Output -- #
# User menu
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """)
    userChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if userChoice.strip() == '1':
        print('Task     |    Priority')
        print('-' * 21)
        for item in table:
            print(item["Task"] + " | " + item["Priority"])
        input('\n[Press enter to return to main menu]')
        continue

    # Step 4 - Add a new item to the list/Table
    elif userChoice.strip() == '2':
        strTask = input('Enter a task: ')
        strPrior = input('Enter a priority[High, Med, Low]: ')
        dicRow = {'Task': strTask.lower(), 'Priority': strPrior.lower()}
        table.append(dicRow)
        print('\nData saved to table...\n'
              '[Press Enter to Return to Main Menu] ')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif userChoice.strip() == '3':
        userRemove = str(input('Please enter the task you would like to delete:\n '))
        for item in table:
            if item['Task'] == userRemove.lower():
                table.remove(item)
                print('\n[', userRemove, ']', 'removed from to-do list.\n'
                                              '[Press Enter to return to main menu]')
                input()
                continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif userChoice.strip() == '4':
        txtFile = open('ToDoList.txt', 'w')
        for item in table:
            txtFile.write(item['Task'] + ' | ' + item['Priority'] + '\n')
        txtFile.close()
        print('-'*21 + '\n')
        print('Data saved to file.\n')
        print('-'*21 + '\n')
        input('[Press Enter to return to main menu]')
        continue

    # Step 7 - Exit program
    elif userChoice.strip() == '5':
        check = input('Are you sure you want to exit? [Y/N]')
        if check.lower() == 'y':
            print('Goodbye!')
            break
        elif check.lower() == 'n':
            continue