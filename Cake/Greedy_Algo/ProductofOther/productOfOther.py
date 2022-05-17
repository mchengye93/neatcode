def get_products_of_all_ints_except_at_index(arr):
	product = [1] * len(arr)
	prefix = 1

	for i in range(len(arr)):
		product[i] *= prefix
		prefix *= arr[i]


	postfix = 1
	for i in range(len(arr)-1, -1 , -1):
		product[i] *= postfix
		postfix *=arr[i]


	return product


arr = [1, 7, 3, 4]

print(get_products_of_all_ints_except_at_index(arr)) # [84, 12, 28, 21]