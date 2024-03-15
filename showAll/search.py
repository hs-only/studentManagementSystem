import json

def searchUtil(jsonFile, roll):
    try:
        with open(jsonFile, 'r') as file:
            data = json.load(file)
            for stud in data:
                if stud['roll'] == roll:
                    return stud
            return None
    except FileNotFoundError:
        print(f"Error: File '{jsonFile}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{jsonFile}' is not a valid JSON file.")
        return None

def search(jsonFile):
    roll=int(input("Enter roll number of student to be searched: "))
    stu=searchUtil(jsonFile,roll)
    if stu:
        print(stu)

