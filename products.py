products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	products.append(name)
	price = input('請輸入商品價格:')  
	products.append([name, price])
print(products)