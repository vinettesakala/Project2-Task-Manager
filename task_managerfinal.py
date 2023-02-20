#====Login Section====
from datetime import datetime, date
usernamelist=[]
passwordlist=[]
 # Reading usernames and passwords from the file and storing in a list
with open ('user.txt','r') as f:
    for line in f:
        username_password = line.split(", ")
        username_password = [s.strip() for s in username_password]
        usernamelist.append(username_password[0])
        passwordlist.append(username_password[1])
        
 # User enters a username and if a incorrect username is entered an error message is displayed
 # User is asked repeatedly to enter a correct username
username = input("Enter your username. ")
while username not in usernamelist:
    print("Incorrect username,please enter a correct username. ")
    username = input("Enter your username. ")
    continue
while username in usernamelist:
    break

 # User enters a password and if a  incorrect password is entered an error message is displayed
 # User is asked repeatedly to enter a correct password 
password = input("Enter your password. ")
while password not in passwordlist:
    print("Incorrect password,please enter a correct password. ")
    password = input("Enter your password. ")
    continue
while password in passwordlist:
    break
    
print("\n")

 # only admin user is allowed to add a new user
 # adding a new user to the user.txt file
 # user is asked to enter new password twice if the two passwords match,
 # the information is added to the file but
 # if they do not match an error message is displayed    
def reg_user():
    """ Adds a new user to the text file."""
    if username == "admin":
        new_username=input("Enter a new username: ")
        while new_username in usernamelist:
            print("Username already exist,add a different username.")
            new_username = input("Enter a new username: ")
            continue
        while new_username not in usernamelist:
            break
        new_password = input("Enter a new password: ")
        password_confirmation = input("Confirm your password: ")
        if new_password == password_confirmation:
            with open ('user.txt','a') as f:
                f.write(new_username + "," + " " + new_password + "\n")
        else:
            print("Incorrect password confirmation!Select option again. ")
    else:
        print("You can not register a new user.")
        

 # adding a new task to task.txt file
 # user is asked to enter the name of the person the task is assigned to,
 # the title of the task,the description of the task,date the task is assigned and,
 # the due date of the task          
def add_task():
    """Adds a task to the text file."""
    with open ('tasks.txt','a') as f:
                   
        person_username=input("Enter the username of the person whom the task is assigned to: ")
        title=input("Enter the title of the task: ")
        description=input("Enter the description of the task: ")
        date_assigned=input("Enter the current date: ")
        due_date=input("Enter the due date of the task: ")
        task_completed=input("Is the task completed? (Yes/No)").capitalize()
            
        f.write(person_username + "," + " " + title +  "," + " " + description + "," + " " + date_assigned + ", " + " " + due_date + "," + " " + task_completed + "\n")
      
        
# code that reads the task from task.txt and prints it    
def view_all():
    """ Reads all the task from file and prints."""
    with open('tasks.txt','r') as f:
                
        for line in f:
            text=line.strip().split(", ")
                    
            print("Task:"+"\t"+"\t"+"\t"+text[1]+"\n"+"Assigned to:"+"\t"+"\t"+text[0]+"\n"+"Date assigned:"+"\t"+"\t"+text[3]
              +"\n"+"Due date:"+"\t"+"\t"+text[4]+"\n"+"Task Complete? "+"\t"+"\t"+"\t"+text[5]+"\n"+"Task description:"+"\n"+text[2] + "\n")
        
            
# code that reads the task from task.txt,check if user logged in has any assigned tasks
# prints the task  
names=[]
def view_mine():
    """Displays tasks assigned to a user."""
            
    with open('tasks.txt','r') as f:
        file_content = f.readlines()
                
        task_completed="No"
        task_number=1
                
        for line in file_content :
            data=line.strip().split(", ")
            names.append(data[0])
                    
            user_task_total=[]
            if username in names and username == data[0] :
                        
                print("Task:"+str(task_number)+"\t"+"\t"+"\t"+data[1]+"\n"+"Assigned to:"+"\t"+"\t"+data[0]+"\n"+"Date assigned:"+"\t"+"\t"+data[3]
              +"\n"+"Due date:"+"\t"+"\t"+data[4]+"\n"+ "Task Complete? "+"\t"+"\t"+"\t"+data[5]+"\n"+"Task description:"+"\n"+data[2] + "\n")
                    
            task_number += 1
                       
        # user selects the task by entering the task number or they press "-1" to go to main menu           
        task_selection=int(input("Enter the number of the task you want to select or enter -1 to return to main menu: "))-1
                    
                               
        if task_selection == -2:
            menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
g - generate reports
s - display statistics
e - Exit
: ''').lower()
     
        else:
                    
            selected_task = file_content[task_selection]
            selected_task=selected_task.split(", ")
                    
            # selects either to mark the task as complete or to edit the task if they havent marked it as complete
            choice=input("Select one of the following options: (mark the task as complete/edit the task) ").lower()
            if choice == "mark the task as complete":
                selected_task[-1] = "Yes\n"
                        
                file_content[task_selection]=", ".join(selected_task)           
                                    
            elif choice == "edit the task" and task_completed == "No":
                person_username=input("Enter the username of the person whom the task is assigned to: ")
                due_date=input("Enter the due date of the task: ")
                selected_task[0]= person_username
                selected_task[4]= due_date
                file_content[task_selection]=", ".join(selected_task)
                    
        with open("tasks.txt","w") as f:
            f.writelines(file_content)
                                           

# code that allows only the admin user to select an option statistics
# code displays the total number of tasks and users
# if any other user selects the option a message is displayed    
def statistics():
    """Displays the number of users and tasks."""
    if username == "admin":
        with open ('tasks.txt','r') as f:
            count_lines = 0
            for line in f:
                if line != "\n":
                    count_lines +=1
                    
            print("Total number tasks: " + "\t" + str(count_lines))

        with open ('user.txt','r') as f:
            count = 0
            for line in f:
                if line != "\n":
                    count +=1
            print("Total number users: " + "\t" + str(count) + "\n")
           
    else:
        print("Invalid option." + "\n")
    
     
# user can generate reports    
def generate_reports():
    """Generate reports."""
    with open ('tasks.txt.','r') as f:
        count_lines = 0
        completed_task_list=[]
        uncompleted_task_list=[]
        over_due_task_list=[]
        for line in f:
            if line != "\n":
                count_lines +=1
                task_total=count_lines   # counts the total number of tasks generated

            data=line.strip().split(", ")
                
            if data[-1].replace("\n","") == "Yes":
                completed_task_list.append(data[-1])  # adds completed tasks to the list
            else:
                uncompleted_task_list.append(data[-1]) # adds uncompleted tasks to the list
                task_due_date=datetime.strptime(data[4], "%d %b %Y").date() # changing date format
                today_date=date.today()
                if today_date >= task_due_date:
                    over_due_task_list.append(data[4]) # adds overdue tasks to the list
                                            
            length1=len(completed_task_list)   # gives the total of completed tasks
            length2=len(uncompleted_task_list) # gives the total of uncompleted tasks
            length3=len(over_due_task_list)    # gives the total of ovedue tasks
            percentage_incomplete_task=length2/task_total * 100  # calculates the percentage of incomplete tasks
            percentage_overdue_task=length3/task_total * 100     # calculates the percentage of overdue tasks
            
        print("Task_overview\n"
              f"Total number of tasks: {task_total}\n"
              f"The total number of completed tasks: {length1}\n"
              f"The total number of uncompleted tasks: {length2}\n"
              f"The total number of tasks that haven't been completed and are ovedue: {length3}\n"
              f"The percentage of tasks that are incomplete: {percentage_incomplete_task}%\n"
              f"The percenage of tasks that are overdue: {percentage_overdue_task}%")

    # text file for tasks overview    
    with open ('tasks_overview.txt','w') as file:
        file.writelines([f"Total number of tasks: {task_total}\n",
                         f"The total number of completed tasks: {length1}\n",
                         f"The total number of uncompleted tasks: {length2}\n",
                         f"The total number of tasks that haven't been completed and are ovedue: {length3}\n",
                         f"The percentage of tasks that are incomplete: {percentage_incomplete_task}%\n",
                         f"The percenage of tasks that are overdue: {percentage_overdue_task}%\n"])
        
    # list of users in user.txt file
    user_list=[]

    # Opening the 'user.txt' file as 'f' in read-mode using the 'open' function.
    with open('user.txt', 'r') as f:
        count = 0
            
        for line in f:
            if line != "\n":
                count +=1
                users_total=count #counts the total number of users
                
            users=line.strip().split(", ")
            user_list.append(users[0])
            
    # list of assigned users
    task_list = []
    # dictionary for completed tasks
    completed_task_dict = {}
    # dictionary for overdue tasks
    overdue_tasks_dict = {}
        
        
    with open("tasks.txt","r") as f:
        for line in f:
            data=line.strip().split(", ")
            task_list.append(data[0])
                
            # calculating the completed tasks assigned to a user
            name = data[0]
            if name in completed_task_dict:
                if data[5] == 'Yes':
                    completed_task_dict[name] += 1
            elif name in completed_task_dict:
                if data[5] == "No":
                    completed_task_dict[name] = 0
            else:
                if data[5] == 'Yes':
                    completed_task_dict[name] = 1
                if data[5] == 'No':
                    completed_task_dict[name] = 0
                
            # calculating overdue tasks assigned to a user
            if name in overdue_tasks_dict:
                due_date = data[4]
                # Changing the format of the 'due_date' variable so that it can be compared.
                due_date = datetime.strptime(due_date, '%d %b %Y').date()
                present=date.today()
                if present > due_date:
                    if data[5] == 'No':
                        overdue_tasks_dict[name] += 1
            elif name in overdue_tasks_dict:
                due_date = data[4]
                due_date = datetime.strptime(due_date, '%d %b %Y').date()
                present=date.today()
                if present > due_date:
                    if data[5] == 'Yes':
                        overdue_tasks_dict[name] = 0
            else:
                due_date = data[4]
                due_date = datetime.strptime(due_date, '%d %b %Y').date()
                present=date.today()
                if present > due_date:
                    if data[5] == 'No':
                        overdue_tasks_dict[name] = 1
                    if data[5] == 'Yes':
                        overdue_tasks_dict[name] = 0
                               
        print("\nUser_overview\n"
             f"Total number of users: {users_total}\n"
             f"The total number tasks: {task_total}\n")

    # Opening the 'user_overview.txt' file as 'file' in write-mode using the 'open' function.
    with open('user_overview.txt','w') as file:
        file.writelines([f"Total number of users: {users_total}\n",
                        f"The total number tasks: {task_total}\n"])
        # Using a for-loop to run through each user in the 'user_list' list
        for user in user_list:
            #counting the number of tasks assigned to a user
            count = task_list.count(user)
            user_task_count = count
            user_completed_tasks = completed_task_dict[user]
            user_overdue_tasks = overdue_tasks_dict[user]
                                                          
            # Calculating the percentage of tasks belonging to user based on the total amount of tasks.
            user_task_perc = (user_task_count / task_total) * 100
            user_task_perc = round(user_task_perc,1)
                    
            # Calculating the percentage of tasks that the user has completed.
            user_complete_perc = (user_completed_tasks / user_task_count) * 100
            user_complete_perc = round(user_complete_perc,1)
                    
            # Calculating the percentage of tasks that the user has NOT completed.
            user_uncompleted_perc = float(100 - user_complete_perc)
                    
            # Calculating the percentage of tasks that the user has overdue.
            user_overdue_perc = (user_overdue_tasks / user_task_count) * 100
            user_overdue_perc = round(user_overdue_perc,1)
                
            print(f"\t{user}\n\tThe total number of tasks assigned to user:\t\t\t\t\t\t{user_task_count}\n\t"
                  f"Percentage of the total number of tasks that have been assigned to user:"
                  f"\t\t{user_task_perc}%\n\t"
                  f"Percentage of the user's tasks that have been completed:\t\t\t\t{user_complete_perc}%\n\t"
                  f"Percentage of the user's tasks that have not been completed:"
                  f"\t\t\t\t{user_uncompleted_perc}%\n\t"
                  f"Percentage of the user's tasks that have not been completed AND are overdue:"
                  f"\t\t{user_overdue_perc}%\n\n")

            # Writing the information to the 'user_overview.txt' file in an easy-to-read format.
            file.writelines([f"\t{user}\n\tThe total number of tasks assigned to user:\t\t\t\t\t\t{user_task_count}\n\t",
                            f"Percentage of the total number of tasks that have been assigned to user:"
                            f"\t\t{user_task_perc}%\n\t",
                            f"Percentage of the user's tasks that have been completed:\t\t\t\t{user_complete_perc}%\n\t",
                            f"Percentage of the user's tasks that have not been completed:"
                            f"\t\t\t\t{user_uncompleted_perc}%\n\t",
                            f"Percentage of the user's tasks that have not been completed AND are overdue:"
                            f"\t\t{user_overdue_perc}%\n\n"])
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
g - generate reports
s - display statistics
e - Exit
: ''').lower()
    if menu == 'r':
        reg_user()

    elif menu == 'a':
         add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == "s":
        statistics()

    elif menu == "g":
        generate_reports()
 
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    else:
        print("You have made a wrong choice, Please Try again")
