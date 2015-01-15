#this module implements all the functions required to preprocess the data statistically

#function to find the mean of a set of numbers
def mean(data_set):
	n = len(data_set)
	sum = 0
	for x in data_set:
		sum+=x
	sum = float(sum)
	return sum/n

#function to mean normalize an array of numbers
def mean_normalize(data_set):
	i = 0
	#converting to float
	for x in data_set:
		data_set[i] = float(x)
		i+=1
	mean_nos = mean(data_set)
	maxm = max(data_set)
	minm = min(data_set)
	i = 0
	sd = maxm - minm
	for x in data_set:
		data_set[i] = (x - mean_nos)/(sd)
		i+=1
	return data_set