import csv, os, sys, constants

# will need to plugin the coordinates
# tl =  39.6, 156.2
# br = 936.0, 441.4
os.system("java -jar tabula.jar -p all -o {0}.csv {0}.pdf".format(sys.argv[1]))

# placeholder string for each student, append this to the csv in the end after all operations
result_current_student = ""

with open(sys.argv[1]) as file:
    reader = list(csv.reader(file))  # list where one list member comprises of one row of the csv
    # will need to think of a way to get number of subjects and subject names
    for row in range(constants.INITIAL_ROW, len(reader), constants.ROWS_PER_PAGE):
        for  student_row in range(0, constants.ROWS_PER_PAGE, constants.LENGTH_EACH_STUDENT):
            # OPERATIONS TO DO HERE



