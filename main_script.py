#SELF-MADE
#import generate_name
from courses import courses
#DEFAULT
import os
import shutil
import docx
from time import ctime
#RUNNING IN FOLDER WHERE DOCS ARE SAVED

currfolder = os.listdir()
newfiles = list()

for files in currfolder:
    if not files.endswith(".py") and os.path.isfile(os.path.join(os.getcwd(), files)):
        newfiles.append(files)
#st_birthtime