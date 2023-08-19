
def SaveToDictionary(): # learned reading from text file from this link: https://www.youtube.com/watch?v=gSbEXZvgyBw
    data= {}
    with open("readfile.txt") as file: 
        for line in file:
            (id, name, time, gender, salary) = line.strip().split(", ")
            data[name] = {
                'ID': id,
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
  


def Admin():
  while(True):
    print("Choose a number: ")
    print("1. Display Statistics")
    print("2. Add an Employee")
    print("3. Display all Employees")
    print("4. Change Employee’s Salary")
    print("5. Remove Employee")
    print("6. Raise Employee’s Salary")
    print("7. Exit")
    choice=int(input())
    if choice==1:
      DisplayStatistics( SaveToDictionary())
    elif choice==2:
      AddEmbloyee()
    elif choice==3:
      DisplayEmployees()
    elif choice==4:
      ChangeSalary()
    elif choice==5:
      RemoveEmployee()
    elif choice==6:
      RaiseSalary()
    elif choice==7:
     break 
    else:
      print("Wrong input")

    
                
print("Welcome to employee data base system!")
userName=(input("Enter your username: "))
password=(input("Enter your password: "))
attempt=0
while attempt<=5:
  if userName=="admin" and password=="admin123123":
     Admin()
     break
   
  elif password=="" and userName in SaveToDictionary():
      Embloyee()
      break
   
  else:
   attempt+=1

