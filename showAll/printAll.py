import json

def show(jsonFile):
    try:
         with open(jsonFile,"r") as file:
            data_=json.load(file)
            print(json.dumps(data_,indent=4))
    except FileNotFoundError:
        print(f"File '{jsonFile}' not found.")
    except json.decoder.JSONDecodeError:
        print(f"Invalid JSON data in file '{jsonFile}'.")