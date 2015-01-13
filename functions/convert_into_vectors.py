#this function converts matrix into individual vectors

def convert_into_vectors(data, num_columns):
	processed_data = []
	for x in xrange(num_columns):
		processed_data.append([]);
	column_counter = 0
	i = 0
	for row in data:
		for i in xrange(num_columns):
			processed_data[i].append(row[i]) 
	return processed_data