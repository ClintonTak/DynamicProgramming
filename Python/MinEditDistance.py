#Given two strings S1 and S2, find out the minimum edit
# distance to transform S1 to S2. 
# Edit operations: insertion, deletion, substitution

def minDist(s1, s2):
	w = len(s1)+1
	h = len(s2)+1
	matrix = [[0 for x in range(w)] for y in range(h)] 

	for i in range(0, len(s1)):
		for j in range(0, len(s2)):
			if (i == 0):
				matrix[i][j] = j
			elif (j == 0):
				matrix[i][j] = i
			elif (s1[i-1]==s2[j-1]):
				matrix[i][j] = matrix[i-1][j-1]
			else:
				matrix[i][j] = 1 + min(min(matrix[i][j-1], matrix[i-1][j]), matrix[i-1][j-1]) 

	return matrix[len(s1)-1][len(s2)-1]



print(minDist("kitten", "sitting"))