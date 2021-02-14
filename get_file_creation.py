import os

def get_file_creation(filename):
    return os.stat(os.path.join(os.getcwd(), filename)).st_birthtime