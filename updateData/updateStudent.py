
import json

def updateDetailsutil(jsonFile, roll):
    try:
        with open(jsonFile, "r+") as file:
            data = json.load(file)

            for student in data:
                if student.get("roll") == roll:
                    print("Current Student Details:")
                    print(json.dumps(student, indent=4))

                    print("Enter modified student details:")
                    newName = input("Enter full name: ")
                    newdob = input("Enter date of birth (YYYY-MM-DD): ")
                    newclass = input("Enter class: ")
                    newsubjects = input("Enter subjects (comma-separated): ").split(',')
                    newmarks = {}
                    for subject in newsubjects:
                        marks = int(input(f"Enter marks for {subject}: "))
                        newmarks[subject] = marks

                    # Update the student's data
                    student["name"] = newname
                    student["dob"] = newdob
                    student["class"] = newclass
                    student["subjects"] = newsubjects
                    student["marks"] = newmarks

                    # Move the file cursor to the beginning of the file
                    file.seek(0)

                    # Write the modified data back to the file
                    json.dump(data, file, indent=4)

                    # Truncate any remaining content (in case the new data is shorter than the old)
                    file.truncate()

                    print(f"Student with Roll Number '{roll}' details updated successfully.")
                    return

            print(f"Student with Roll Number '{roll}' not found.")
    except FileNotFoundError:
        print(f"File '{jsonFile}' not found.")

def updateDetails(jsonFile):
    roll=int(input("Enter the roll number of student to update data "))
    updateDetailsutil(jsonFile,roll)