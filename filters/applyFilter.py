from . import allFilters
from students.student import student
from datetime import datetime
import json

def decideFilter(parameter):
    if parameter=="class":
        return allFilters.classFilter
    if parameter=="age":
        return allFilters.ageFilter
    if parameter=="grade":
        return allFilters.gradeFilter
    if parameter=="dob":
        return allFilters.dobFilter

def applyFilterutil(stu,lst,criteria):
    flag=True
    for i in range(len(lst)):
        fun=decideFilter(lst[i])
        flag=flag and (fun(criteria,stu))
    
    return flag

def applyFilter(jsonFile):
    print("Select Filter to be applied")
    string = '''1.Age\n2.Class\n3.Grade\n4.DOB\n'''
    print(string)
    dict_ = {1: "age", 2: "class", 3: "grade", 4: "dob"}
    choice = int(input())
    criteria = []
    if choice == 1:
        criteria.append(int(input("Enter minimum age: ")))
        criteria.append(int(input("Enter maximum age: ")))
    elif choice == 2:
        criteria.append(input("Enter class: "))
    elif choice == 3:
        criteria.append(input("Enter grade: "))
    elif choice == 4:
        d1 = input("Enter lower bound: ")
        d2 = input("Enter upper bound: ")
        criteria.append(datetime.strptime(d1, '%Y-%m-%d'))
        criteria.append(datetime.strptime(d2, '%Y-%m-%d'))

    with open(jsonFile, 'r') as file:
        data = json.load(file)
        for stud in data:
            temp=student(stud)
            if applyFilterutil(temp,[dict_[choice]],criteria):
                print(stud)