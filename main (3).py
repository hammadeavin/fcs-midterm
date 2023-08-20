import datetime

def SaveToDictionary():
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

def DisplayStatistics(data):
    gender_count = {'male': 0, 'female': 0}

    for employee in data.values():
        gender = employee['Gender']
        if gender in gender_count:
            gender_count[gender] += 1

    print("Number of males:", gender_count['male'])
    print("Number of females:", gender_count['female'])

def AddEmployee(data):
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

def generate_emp_id(data):
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
def DisplayEmployees():
  file=open("readfile.txt","r")
  contents=file.read()
  print(contents)
  file.close()
  # apdate the salary by reading from the file, looping through it to check if the id matches and then writing to it to change the salary
def ChangeSalary():
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


def Admin():
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
            # RemoveEmployee()
            pass
        elif choice == 6:
            # RaiseSalary()
            pass
        elif choice == 7:
            break
        else:
            print("Wrong input")

print("Welcome to the employee database system!")
userName = input("Enter your username: ")
password = input("Enter your password: ")
attempt = 0
while attempt <= 5:
    if userName == "admin" and password == "admin123123":
        Admin()
        break
    elif password == "" and userName in SaveToDictionary():
        # Embloyee()
        break
    else:
        attempt += 1
        print("Incorrect Username and/or Password")
        break