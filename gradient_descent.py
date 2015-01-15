"""
Program to implement gradient descent
"""
#imports
import imports
from file_to_array_functions import read_into_array_from_file
from convert_into_vectors import convert_into_vectors
import numpy as np
from matplotlib import pyplot as plt
from misc_func import *

data = read_into_array_from_file(get_datasets_path()+'/BrainWeight_BodyWeight.txt' , True , 'float')
data = convert_into_vectors(data,2)

#initialising theta_0 and theta_1 and alpha(the learning rate)
theta_0 = 0.0
theta_1 = 0.0
alpha = 0.00000000001
#data = np.loadtxt('BrainWeight_BodyWeight.txt',dtype='float', comments='#',delimiter=None,converters=None,skiprows=0,usecols=[1,2])
#BrainWeight , BodyWeight = data.T
#plt.scatter(BrainWeight,BodyWeight)
BrainWeight = data[0]
BodyWeight = data[1]
#number of training examples
m = len(BrainWeight)
num_iterations = 5
for x in xrange(num_iterations):
	sum = 0
	for i in xrange(m):
		sum = sum + (calculate_hypothesis_function(theta_0,theta_1,BrainWeight[i]) - BodyWeight[i])
	temp_0 = theta_0 - (alpha * (1.0/m) * sum)
	sum = 0
	for i in xrange(m):
		sum = sum + ((calculate_hypothesis_function(theta_0,theta_1,BrainWeight[i]) - BodyWeight[i])) * BrainWeight[i]
	temp_1 = theta_1 - (alpha * (1.0/m) * sum)
	theta_0 = temp_0
	theta_1 = temp_1
	print "Iteration number: "+str(x)
	for a in xrange(m):
		print str(calculate_hypothesis_function(theta_0,theta_1,BodyWeight[a]))+" "+str(BodyWeight[a])+"\n"
# i = 0
# predicted_body_weight = []
# for x in BrainWeight:
# 	predicted_body_weight.append(calculate_hypothesis_function(theta_0,theta_1,BrainWeight[i]))
# 	print (predicted_body_weight[i] - BodyWeight[i])**2
# 	i+=1

# print theta_0
# print theta_1
# print BodyWeight
# print "\n\n"
# print predicted_body_weight
