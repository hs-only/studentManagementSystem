from students.student import student
from showAll import search,printAll
import json

def classAverageUtil(jsonFile,clas):
    with open(jsonFile,"r") as file:
        data=json.load(file)
        totalStudents=0
        Totalpercentage=0.0
        for stud in data:
            if stud["class"]==clas:
                totalStudents+=1
                Totalpercentage+=student(stud).percentage()
        if totalStudents!=0:
            avg=Totalpercentage/totalStudents
            print(f"average of class {clas} = {avg}")
        else:
            print(f"No student of class {clas}")

def classAverage(jsonFile):
    clas=input("Enter class whose average is to be calculated ")
    classAverageUtil(jsonFile,clas)


def studentAverage(jsonFile):
    roll=int(input("Enter roll of studnet: "))
    stu=search.searchUtil(jsonFile,roll)
    if len(stu['marks'])>0:
        print("average marks of the studnet=",sum(stu["marks"].values())/len(stu["marks"]))
    else:
        print(0)

