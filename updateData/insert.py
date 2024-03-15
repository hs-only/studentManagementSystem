import json

def getNextRoll(rollFile):
    try:
        with open(rollFile, 'r+') as file:
            next_roll = int(file.read().strip())
            file.seek(0)
            file.write(str(next_roll + 1))
            return next_roll
    except FileNotFoundError:
        print(f"Error: File '{rollFile}' not found.")
        return None
    except ValueError:
        print(f"Error: '{rollFile}' does not contain a valid integer.")
        return None

def insertUtil(jsonFile, stud):
    rollFile=r"C:\codes\student_management_system\updateData\updateRoll.txt"
    stud["roll"]=getNextRoll(rollFile)
    try:
        # Open the file in append mode
        with open(jsonFile, "a+") as file:
            # Move the file cursor to the end of the file
            file.seek(0, 2)

            # Check if the file is empty
            file_position = file.tell()
            if file_position == 0:
                # If the file is empty, write an opening bracket to start a JSON array
                file.write("[\n")
            else:
                # If the file is not empty, move the file cursor back to the last character
                file.seek(file_position - 1)
                last_char = file.read(1)
                if last_char == "]":
                    # If the last character is a closing bracket, truncate it
                    file.seek(file_position - 2)
                    file.truncate()
                    # Move the file cursor back to the new end of the file
                    file.seek(0, 2)
                    file.write(",\n")
                else:
                    # If the last character is not a closing bracket, write a comma to separate objects
                    file.write(",\n")

            # Write the new object to the file
            json.dump(stud, file, indent=4)
            file.write("\n]")

        print("Object appended to the JSON file successfully.")
    except FileNotFoundError:
        print(f"File '{jsonFile}' not found.")

def insert(jsonFile):
    stud = {}

    stud['name'] = input("Enter student name: ")
    stud['dob'] = input("Enter date of birth (YYYY-MM-DD): ")
    stud['class'] = input("Enter class: ")

    # Taking subjects and marks input
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = []
    marks = {}
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1}: ")
        mark = float(input(f"Enter marks for {subject}: "))
        subjects.append(subject)
        marks[subject]=mark

    stud['subjects'] = subjects
    stud['marks'] = marks

    insertUtil(jsonFile,stud)
    
