import os


def load_student():
    if not os.path.exists("student.txt"):
        userresponse=input("No user file found, create new? (y/n) ")
        if userresponse == "y" or userresponse=="Y":
            firstname = input("Enter your first name: ")
            surname = input("Enter your last name: ")
            classname = input("Enter you class name: ")
            with open("student.txt", "w") as f:
                f.write(f"FIRSTNAME:{firstname}\nSURNAME:{surname}\nCLASSNAME:{classname}")
        else:
            return False
    with open('student.txt', 'r') as f:
        lines = f.readlines()
        read_firstname = lines[0].split(":")[1].strip()
        read_surname = lines[1].split(":")[1].strip()
        read_classname = lines[2].split(":")[1].strip()
        return {"FIRSTNAME":read_firstname,"SURNAME":read_surname,"CLASSNAME":read_classname}
