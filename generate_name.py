import read_file
import courses



def generate_docname(subject, string):
    coursedict = courses.courses
    currentstudent = read_file.load_student()
    return subject+currentstudent["CLASSNAME"]+currentstudent["FIRSTNAME"]+currentstudent["SURNAME"]+string
