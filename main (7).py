import datetime

def SaveToDictionary():#O(n), where 'n' is the number of lines in the file
    data = {}
    with open("readfile.txt") as file:
        for line in file:
            (emp_id, name, time, gender, salary) = line.strip().split(", ")
            data[name] = {
                'ID': emp_id,
                'Date': time,
                'Gender': gender,
                'Salary': int(salary)
            }
    return data

def DisplayStatistics(data):#O(n),'n' is the number of employees in the data dictionary. 
    gender_count = {'male': 0, 'female': 0}

    for employee in data.values():
        gender = employee['Gender']
        if gender in gender_count:
            gender_count[gender] += 1
    print("Number of males:", gender_count['male'])
    print("Number of females:", gender_count['female'])

def AddEmployee(data):#function is O(1)
    emp_id = generate_emp_id(data)
    name = input("Enter user name: ")
    gender = input("Enter the gender of the employee: ")
    salary = int(input("Enter the salary: "))
    
    current_datetime = datetime.datetime.now().strftime("%Y%m%d")
    
    data[name] = {
        'ID': emp_id,
        'Date': current_datetime,
        'Gender': gender,
        'Salary': salary
    }
    
    # Save the added data back to the file
  #learned how to write to the file from this link: https://www.youtube.com/watch?v=E1gDJU9Q4k

    with open("readfile.txt", "a") as file:
        file.write(f"\n{emp_id}, {name}, {current_datetime}, {gender}, {salary}")

def generate_emp_id(data):#O(n), where n is the number of employees in the data dictionary.
    highest_id = 0
    for employee in data.values():
        emp_id = employee['ID']
        emp_num = int(emp_id[3:])
        if emp_num > highest_id:
            highest_id = emp_num
    new_id = highest_id + 1
    return f"emp{new_id:03d}"
  
  # display all the contents in the text file
#learned from this link: https://www.youtube.com/watch?v=12aQkP7Y6i4
def DisplayEmployees():#O(n),n is the number of lines in the file.
  file=open("readfile.txt","r")
  contents=file.read()
  print(contents)
  file.close()
  
  # apdate the salary by reading from the file, looping through it to check if the id matches and then writing to it to change the salary
def ChangeSalary():#O(n),n is the number of lines in the file.
    emp_id = input("Enter Employee's ID: ")
    new_salary = input("Enter the new salary: ")

    employee_records = []

    with open("readfile.txt", "r") as f:
        for line in f:
            emp_id, name, time, gender, salary = line.strip().split(", ")
            if emp_id == emp_id:
                employee_records.append((emp_id, name, time, gender, new_salary))
            else:
                employee_records.append((emp_id, name, time, gender, salary))

    with open("readfile.txt", "w") as f:
        for record in employee_records:
            emp_id, name, time, gender, salary = record
            f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, time, gender, salary))

    print("Salary updated successfully!")
#Function to remove employee from the file if the id input mathches with that in the file
def RemoveEmployee():#O(n),n is the number of lines in the file
    emp_id = input("Enter Employee's ID to remove: ")

    employee_records = []

    # Open the file in read mode
    with open("readfile.txt", "r") as f:
        # Loop through each line in the file
        for line in f:
            # Split the line into its contents
            emp_id_file, name, time, gender, salary = line.strip().split(", ")
            # Check if the emp_id from the file matches the input emp_id
            # If IDs match, the record is not added
            if emp_id_file != emp_id:
                # If no match, add the record to the employee_records list
                employee_records.append((emp_id_file, name, time, gender, salary))

    # Open the file in write mode to update its content
    with open("readfile.txt", "w") as f:
        # Loop through the employee records to rewrite the file without the deleted             record
        for record in employee_records:
            emp_id, name, time, gender, salary = record
            # Write the record to the file
            f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, time, gender, salary))

    print("Employee record removed successfully!")

# Function to raise the employee's salary if found by entering the percentage
def RaiseSalary():#function is O(n),n is the number of lines in the file
    emp_id_input = input("Enter Employee's ID: ")
    percentage = float(input("Enter the percentage: "))
    employee_records = []
    with open("readfile.txt", "r") as f:
        for line in f:
            emp_id, name, time, gender, salary = line.strip().split(", ")
          #if id matches the salary will be raised and added to the employee records
            if emp_id == emp_id_input:
                salary = float(salary) 
                raised_salary = round(salary + salary * (percentage / 100))
                employee_records.append((emp_id, name, time, gender, raised_salary))
              #otherwise the salary will remain the same
            else:
                employee_records.append((emp_id, name, time, gender, salary))
    with open("readfile.txt", "w") as f:
        for record in employee_records:
            emp_id, name, time, gender, salary = record
            f.write("{}, {}, {}, {}, {}\n".format(emp_id, name, time, gender, salary))
    print("Salary raised successfully!")

# A fuction to display the salary of the user
def CheckSalary(userName):#function is O(n),n is the number of lines in the file
    with open("readfile.txt", "r") as f:
        for line in f:
            emp_id, name, time, gender, salary = line.strip().split(", ")
            if userName==name:
              print("Salary:", salary)
            else:
              print("user name not found")

def Exit(login_time):#function is O(n),n is the number of lines in the file
   with open("readfile.txt", "r") as f:
        lines = f.readlines()
   with open("readfile.txt", "w") as f:
        for line in lines:
            if userName in line:
                emp_id, name, time, gender, salary = line.strip().split(", ")
                updated_line = f"{emp_id}, {name}, {login_time}, {gender}, {salary}\n"
                f.write(updated_line)
            else:
                f.write(line)

        print("Logged out successfully.")
# A fuction if the user is an admin  
def Admin():# O(n), where n is the number of lines in the file.
    while True:
        print("Choose a number: ")
        print("1. Display Statistics")
        print("2. Add an Employee")
        print("3. Display all Employees")
        print("4. Change Employee’s Salary")
        print("5. Remove Employee")
        print("6. Raise Employee’s Salary")
        print("7. Exit")
        choice = int(input())
        if choice == 1:
            DisplayStatistics(SaveToDictionary())
        elif choice == 2:
            AddEmployee(SaveToDictionary())
        elif choice == 3:
             DisplayEmployees()
        elif choice == 4:
             ChangeSalary()
        elif choice == 5:
             RemoveEmployee()
        elif choice == 6:
             RaiseSalary()
        elif choice == 7:
            break
        else:
            print("Wrong input")
          
#A function if the user is an employee          
def Employee(userName):# O(n),n is the number of lines or records in the file.
  login_time = datetime.datetime.now().strftime("%Y%m%d")
  print("Choose a number: ")
  print("1. Chek my salary")
  print("2. Exit")
  choice=int(input())
  if choice==1:
    CheckSalary(userName)
  if choice==2:  
    Exit( login_time)
    
print("Welcome to the employee database system!")
userName = input("Enter your username: ")
password = input("Enter your password: ")
attempt = 0
while attempt <= 5:
    if userName == "admin" and password == "admin123123":
        Admin()
        break
    elif password == "" and userName in SaveToDictionary():
      Employee(userName)
      break
    else:
        attempt += 1
        print("Incorrect Username and/or Password")
        break
      
