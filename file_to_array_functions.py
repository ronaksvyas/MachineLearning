"""
This function takes input a filename and a couple of other parameters and converts it into an array and returns it.
filename is the name of the file.
ignore_first_column is a boolean argument set to true if you want to ignore the first column of the file. 
number_type is a string argument which supports integer and float. This argument is about how you want your numbers. 
"""
import os
def read_into_array_from_file(filename, ignore_first_column, number_type = 'float'):
    #check if a file is present with that name in the current directory
    file_exist = os.path.isfile(filename)
    if(file_exist == False):
        print 'The file you mentioned doesn\'t exist'
        return False
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    i = 0
    for row in content:
        temp = content[i].split()
        content[i] = temp
        j = 0
        for x in content[i]:
            temp = float(x)
            if(number_type == 'int'):
                temp = int(x)
            content[i][j] = temp
            j = j + 1
        i = i + 1
    if(ignore_first_column == True):
        for row in content:
            row.pop(0)
    return content
