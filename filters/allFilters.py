from students import student
from datetime import datetime

def ageFilter(criteria,stu):
    age=stu.calculateAge()
    return (age>=criteria[0] and age<=criteria[1])

def classFilter(criteria, stu):
    return stu.class_==criteria[0]

def dobFilter(criteria,stu):
    dob_=datetime.strptime(stu.dob,'%Y-%m-%d')
    return (dob_>=criteria[0] and dob_<=criteria[1])

def gradeFilter(criteria,stu):
    g=stu.calculateGrade()
    return g==criteria[0]