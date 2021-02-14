import load_student
import courses



def generate_docname(subject, string):
    coursedict = courses.courses
    currentstudent = load_student.load_student()
    return subject+currentstudent["CLASSNAME"]+currentstudent["FIRSTNAME"]+currentstudent["SURNAME"]+string
