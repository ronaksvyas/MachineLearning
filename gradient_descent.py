"""
Program to implement gradient descent
"""
#imports
from file_to_array_functions import read_into_array_from_file
from convert_into_vectors import convert_into_vectors
import numpy as np
from matplotlib import pyplot as plt

data = read_into_array_from_file('BrainWeight_BodyWeight.txt' , True , 'float')
data = convert_into_vectors(array,4)

#initialising theta_0 and theta_1 and alpha(the learning rate)
theta_0 = 0
theta_1 = 0
alpha = 0.5
#data = np.loadtxt('BrainWeight_BodyWeight.txt',dtype='float', comments='#',delimiter=None,converters=None,skiprows=0,usecols=[1,2])
#BrainWeight , BodyWeight = data.T
#plt.scatter(BrainWeight,BodyWeight)
BrainWeight = data[0]
BodyWeight = data[1]
