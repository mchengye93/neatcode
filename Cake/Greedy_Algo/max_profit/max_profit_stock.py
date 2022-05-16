def max_profit_stock(stock_prices):
	if len(stock_prices) < 2:
		return -1
	minPrice = stock_prices[0]

	maxProfit = stock_prices[1]-stock_prices[0]

	for stock_price in stock_prices:
		profit = stock_price - minPrice
		maxProfit = max(maxProfit,profit)

		minPrice = min(minPrice, stock_price)

	return maxProfit

stock_prices = [10, 7, 5, 8, 11, 9]

print(max_profit_stock(stock_prices))