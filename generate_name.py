import read_file
import courses

coursedict = courses.courses
currentstudent = read_file.load_student()

def generate_docname(subject, string):
    return subject+currentstudent["CLASSNAME"]+currentstudent["FIRSTNAME"]+currentstudent["SURNAME"]+string

print(generate_docname("TY", "MeinHobby2"))