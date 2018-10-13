import csv
import os
import sys
import constants
import re


def convert2csv(filename):
    os.system(f'java -jar tabula-1.0.2-jar-with-dependencies.jar -p all -a {constants.Y1},{constants.X1},{constants.Y2},{constants.X2} -o {filename}.csv {filename}.pdf')


convert2csv(sys.argv[1])

# placeholder string for each student, append this to the csv in the end after all operations
result_current_student = ""


def get_marks(row1, row2, row3, row4):
    row1_tokens = row_search(row1)
    row2_tokens = row_search(row2)
    row3_tokens = row_search(row3)
    row4_tokens = row_search(row4)
    # first subject
    index = 0
    for token in row1_tokens:
        match = re.search("\d+", token)
        if match:
            index = row1_tokens.index(token)
            break

    marks1 = row1_tokens[index: index + 5] + row2_tokens[1:4]
    # row 2 tokens are wrong for now, will printout wrong stuff if name leaks
    return marks1


def row_search(r):
    tokens = re.findall("[.\d\w()\-+]+", r)
    return tokens


with open(sys.argv[1]) as file:
    csv_r = list(csv.reader(file))  # list where one list member comprises of one row of the csv
    # will need to think of a way to get number of subjects and subject names
    reader = []

    for line in csv_r:
        current_line = " ".join(line)
        reader.append(current_line)

    for row in range(constants.INITIAL_ROW, len(reader), constants.ROWS_PER_PAGE):
        for student_row in range(0, constants.ROWS_PER_PAGE, constants.LENGTH_EACH_STUDENT):
            name_current_student = reader[row + student_row][0].split()
            result_current_student += name_current_student[0] + ", " + " ".join(name_current_student)[len(name_current_student[0]):] + ", "
            sub1_marks = get_marks(reader[student_row + 0], reader[student_row + 1])

            result_current_student = str(sub1_marks)
            print(result_current_student)
