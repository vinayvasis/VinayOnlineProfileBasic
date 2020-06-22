# [1,4,99,3,5,2,100]
# [100,99,5,4,3,2,1]
	# lf = []
	# value.sort(reverse = True)
	# v = 1
	# for num in value:
	# 	if num - 1 == value[v]:
	# 		lf.append(num)
	# 		v+=1
	# lf.append(lf[-1] -1) 
def find_sequence(value):
	lg = set()
	lf =[]
	g = []
	j = 0
	# print(value)
	# for num in value:
	# 	if num == 1:
	# 		lg.add(num)
	# 		value.remove(num)
	# 	else:
	# 		if num+1 in value and num-1 in value:
	# 			lg.add(num)

	# print(lg,lf)		
	# return sum(lf)
	for num in value:
		if num+1 in value:
			lf.append(num)
			lf.append(num+1)
			for x in lf:
				if x + 1 in value:
					lf.append(x+1) 
	print(lf)
print(find_sequence([1,4,99,3,5,2,100,98,97]) == 394)  	