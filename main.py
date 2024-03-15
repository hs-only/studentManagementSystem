import numpy as np
import json
import os
from filters import applyFilter
from bonusFeatures import bonus
from showAll import printAll,search
from students import student
from updateData import deleteStudent,insert,updateStudent

def console(jsonFile):
    string="""\n1.Show All Students\n2.Filter students\n3.Search Student\n4.Add a student\n5.Update a student'srecord\n6.Delete a student\n7.Get average percentage of a class\n8.Get average marks of student\n9.Exit
    """
    while (1):
        print(string)
        choice=int(input("Enter your choice "))
        if choice==1:
            printAll.show(jsonFile)
        elif choice==2:
            applyFilter.applyFilter(jsonFile)
        elif choice==3:
            search.search(jsonFile)
        elif choice==4:
            insert.insert(jsonFile)
        elif choice==5:
            updateStudent.updateDetails(jsonFile)
        elif choice==6:
            deleteStudent.delete(jsonFile)
        elif choice==7:
            bonus.classAverage(jsonFile)
        elif choice==8:
            bonus.studentAverage(jsonFile)
        elif choice==9:
            break
        else:
            print("Invalid choice !!!")


if __name__=="__main__":
    jsonFile=r"C:\codes\student_management_system\studentsData.json"
    console(jsonFile)