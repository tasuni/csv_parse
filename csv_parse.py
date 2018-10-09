import csv, os, sys
import constants as c

def convert2csv(filename):
    os.system(
        f'java -jar tabula-1.0.2-jar-with-dependencies.jar -p all -a {c.Y1},{c.X1},{c.Y2},{c.X2} -o {filename}.csv {filename}.pdf')

    
# placeholder string for each student, append this to the csv in the end after all operations
result_current_student = ""
convert2csv(sys.argv[1])

with open(sys.argv[1]) as file:
    reader = list(csv.reader(file))  # list where one list member comprises of one row of the csv
    # will need to think of a way to get number of subjects and subject names
    for row in range(constants.INITIAL_ROW, len(reader), constants.ROWS_PER_PAGE):
        for  student_row in range(0, constants.ROWS_PER_PAGE, constants.LENGTH_EACH_STUDENT):
            # OPERATIONS TO DO HERE
