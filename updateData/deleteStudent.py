import json

def deleteUtil(jsonFile, student_roll):
    try:
        with open(jsonFile, "r+") as file:
            data = json.load(file)
            cnt=0
            i=0
            for student in data:
                if student['roll']==student_roll:
                    del data[i]
                    cnt+=1
                i+=1

            file.seek(0)

            # Write the modified data back to the file
            json.dump(data, file, indent=4)

            # Truncate any remaining content (in case the new data is shorter than the old)
            file.truncate()

        print(f"'{cnt}'student deleted successfully.")
    except FileNotFoundError:
        print(f"File '{jsonFile}' not found.")

def delete(jsonFile):
    print("Enter roll number: ")
    roll_number = input()
    deleteUtil(jsonFile,roll_number)