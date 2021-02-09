'''
https://www.acmicpc.net/problem/14501

퇴사 문제.
'''

import numpy as np
from sys import stdin

timelist = []
worthlist = []

def main():
	n = int(stdin.readline())
	if not (n >=1) & (n <=15):
		raise ValueError

	
	for x in range(0,n):
		line = stdin.readline()
		t, w = line.split()
		t = int(t)
		w = int(w)
		if not (t >=1) & (t <=5):
			raise ValueError
		if not (w >=1) & (w <=1000):
			raise ValueError
			
		timelist.append(t)
		worthlist.append(w)
	

	max_worth = 0
	for x in range(0,n): # 0~14
		profit = func(0,n,x)
		try:
			if profit > max_worth:
				max_worth = profit
		except:
			print('day {} trial is failed!'.format(x+1))
	print(max_worth)

def func(profit,max_date,cur_date):
	#print('cur_date',cur_date)
	#print('profit ',profit)
	if max_date <= cur_date:
		return profit
	if max_date < (cur_date + timelist[cur_date]):
		return profit
	else:
		profit += worthlist[cur_date]
		cur_date += timelist[cur_date]
		profit = func(profit, max_date, cur_date)
	return profit


if __name__ == '__main__':
	main()