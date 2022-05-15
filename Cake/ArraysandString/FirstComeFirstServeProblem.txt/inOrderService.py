 #  Take Out Orders: [1, 3, 5]
 # Dine In Orders: [2, 4, 6]
 #  Served Orders: [1, 2, 4, 6, 5, 3]

def inOrder(take_out_orders, dine_in_orders, served_orders):
	x = 0
	y = 0

	for order in served_orders:
		if x < len(take_out_orders) and order == take_out_orders[x]:
			x+=1
			continue
		elif y < len(dine_in_orders) and order == dine_in_orders[y]:
			y+=1
			continue
		else:
			return False
	return True

#  Take Out Orders: [1, 3, 5]
 # Dine In Orders: [2, 4, 6]
 #  Served Orders: [1, 2, 4, 6, 5, 3]

take_out_orders = [1, 3, 5]
dine_in_orders = [2, 4, 6]
server_orders = [1, 2, 4, 6, 5, 3]

print(inOrder(take_out_orders ,dine_in_orders,server_orders)) # False

take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
server_orders = [17, 8, 12, 19, 24, 2]

print(inOrder(take_out_orders ,dine_in_orders,server_orders)) # True