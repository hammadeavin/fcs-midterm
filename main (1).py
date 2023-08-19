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
print(SaveToDictionary())    
  