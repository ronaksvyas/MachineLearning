"""
Program to implement gradient descent
"""

from file_to_array_functions import read_into_array_from_file
from convert_into_vectors import convert_into_vectors
array = read_into_array_from_file('test_dataset.txt' , True , 'float')
print array
array = convert_into_vectors(array,4)
print array