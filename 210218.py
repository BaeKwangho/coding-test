from copy import deepcopy
if __name__ == '__main__':
	def invade(pos):
		i,j = pos
		if (i-1)>=0:
			if array_copy[i-1][j]==0:
				array_copy[i-1][j]=2
				invade((i-1,j))
		if (i+1)<n: 
			if array_copy[i+1][j]==0:
				array_copy[i+1][j]=2
				invade((i+1,j))
		if (j-1)>=0: 
			if array_copy[i][j-1]==0:
				array_copy[i][j-1]=2
				invade((i,j-1))	
		if (j+1)<m: 
			if array_copy[i][j+1]==0:
				array_copy[i][j+1]=2
				invade((i,j+1))

	def count_array():
		num = 0
		for i in range(n):
			for j in range(m):
				if array_copy[i][j] == 0:
					num+=1
		return num	

	def copy_array():
		for i in range(n):
			for j in range(m):
				array_copy[i][j] = array[i][j]
				
	n, m = map(int, input().split())
	array = [[[] for i in range(n)] for j in range(m)]
	virus = []
	empty = []
	for i in range(n):
		row = [int(t) for t in input().split()]
		for j,val in enumerate(row):
			if val==2:
				virus.append([i,j])
			if val==0:
				empty.append([i,j])
		array[i] = row
	area = len(empty)
	maximum = 0
	res_arr = []
	array_copy = deepcopy(array)
	for first in range(area-2):
		for second in range(first+1,area-1):
			for third in range(first+2,area):
				copy_array()
				array_copy[empty[first][0]][empty[first][1]]=1
				array_copy[empty[second][0]][empty[second][1]]=1
				array_copy[empty[third][0]][empty[third][1]]=1
				for v in virus:
					invade(v)
				result = count_array()
				if maximum < result:
					maximum = result
	print(maximum)