import csv
import os
import sys
import constants
import re

# will need to plugin the coordinates
# tl =  39.6, 156.2
# br = 936.0, 441.4
os.system("java -jar tabula.jar -p all -o {0}.csv {0}.pdf".format(sys.argv[1]))

# placeholder string for each student, append this to the csv in the end after all operations
result_current_student = ""

with open(sys.argv[1]) as file:
    reader = list(csv.reader(file))  # list where one list member comprises of one row of the csv
    # will need to think of a way to get number of subjects and subject names

    for line in reader:
        line = " ".join(line)

    for row in range(constants.INITIAL_ROW, len(reader), constants.ROWS_PER_PAGE):
        for student_row in range(0, constants.ROWS_PER_PAGE, constants.LENGTH_EACH_STUDENT):
            name_current_student = reader[row + student_row][0].split()
            result_current_student += name_current_student[0] + ", " + " ".join(name_current_student)[len(name_current_student[0]):] + ", "


def get_marks(row1, row2, row3, row4):
    marks1 = []
    marks2 = []
    marks3 = []
    marks4 = []
    marks5 = []
    marks6 = []

    # first subject
    index = 0
    row1_tokens = re.findall("[\.\d\w\(\)\-\+]+", row1)
    for token in row1_tokens:
        match = re.search("\d+", token)
        if match:
            index = row1_tokens.index(token)
            break

    
