def merge_lists(list1, list2):
	ans = []


	i = 0
	x = 0


	while i < len(list1) and x < len(list2):
		if list1[i] < list2[x]:
			ans.append(list1[i])
			i +=1
		else:
			ans.append(list2[x])
			x +=1

	while i < len(list1):
		ans.append(list1[i])
		i +=1

	while x < len(list2):
		ans.append(list2[x])
		x +=1

	return ans

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists(my_list, alices_list)