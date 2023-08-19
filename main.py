def SaveToDictionary(): # I've learned dealing with file from here    https://www.youtube.com/watch?v=ZCmdm-RuRFA&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=30&ab_channel=Codezilla
    data= {}
    with open("readfile.txt") as file: # Converting to dictionary from here   https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
        for line in file:
            (id, name, time, gender, salary) = line.strip().split(", ")
            data[name] = {
                'ID': id,
                'Date': time,
                'Gender': gender,
                'Salary': int(salary)
            }
    # print(d)  it was just for reference
    return data
print(SaveToDictionary())    
  