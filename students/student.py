import numpy as np
from datetime import datetime
class student:
    def __init__(self,data):
        self.roll=data['roll']
        self.name=data['name']
        self.dob=data['dob']
        self.class_=data['class']
        self.subjects=data['subjects']
        self.marks=data['marks']
    
    #percentage
    def percentage(self):
        return (sum(self.marks.values())/(100*len(self.subjects)))*100.0
    
    def calculateGrade(self):
        per=self.percentage()
        if per>=90.0:
            return "A+"
        elif per>=80:
            return "A"
        elif per>=70:
            return "B"
        elif per>=60:
            return "C"
        elif per>=50:
            return "D"
        else:
            return "F"
    
    def calculateAge(self):
        today=datetime.today()
        dob_=datetime.strptime(self.dob,"%Y-%m-%d")
        age=today.year-dob_.year-((today.month,today.day)<(dob_.month,dob_.day))
        return age



