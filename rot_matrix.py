def rotate(l):
	
	answer = []
	
	for i in range(0,len(l[0])):
		temp = []
		for j in range(len(l[0])-1,-1,-1):
			temp.append(l[j][i])
		answer.append(temp)
	return answer
	
rotate([[1,2,3],[4,5,6],[7,8,9]])
