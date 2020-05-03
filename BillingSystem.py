''' Super Market Billing System '''

# Global Variables
Cart = {}
Amount = 00.00
Total_Amount = 00.00
Items_List = {
	1:  {'Name': 'Apple',        'Qty': 26, 'Price':20.00},
	2:  {'Name': 'Mango',        'Qty': 31, 'Price':20.00},
	3:  {'Name': 'Guava',        'Qty': 42, 'Price':15.00},
	4:  {'Name': 'Strawberries', 'Qty': 31, 'Price':15.00},
	5:  {'Name': 'Banana',       'Qty': 35, 'Price':7.00},
	6:  {'Name': 'Watermelon',   'Qty': 21, 'Price':25.00},
	7:  {'Name': 'Grapes',       'Qty': 53, 'Price':20.00},
	8:  {'Name': 'Orange',       'Qty': 21, 'Price':20.00},
	9:  {'Name': 'Pineapple',    'Qty': 14, 'Price':30.00},
	10: {'Name': 'Pomegranate',  'Qty': 36, 'Price':10.00}
}

# Function to show products available
def ShowItems():
	print("\nNo. Products      Qty   Price")
	print('-----------------------------')
	for i in Items_List:
		print('%-2d  %-12s  %2d    %.2f' %(i, Items_List[i]['Name'], Items_List[i]['Qty'], Items_List[i]['Price']))

# Function to Add Items
def AddItem():
	global Amount, Total_Amount
	ShowItems()
	while (True):
		try:
			Product = int(input("\nEnter the product no. : "))
			Quantity = int(input("Enter no. of items : "))
			if Product not in Items_List:
				print("Enter products available")
			elif Quantity > Items_List[Product]['Qty'] :
				print("Stock is not sufficient")
			elif Quantity == 0:
				print("Select items")
			else:
				Items_List[Product]['Qty'] -= Quantity
				break
		except:
			print("Enter valid number")
	for i in range(1):
		j = len(Cart)
		Cart.update({
			j+1 : {
				'Name': Items_List[Product]['Name'],
				'Quantity': Quantity,
				'Price': Items_List[Product]['Price']
			}
		}
		)
	print("\nProducts      Qty   Price")
	print("-------------------------")
	for i in Cart:
		print('%-12s  %2d    %.2f' % (Cart[i]['Name'], Cart[i]['Quantity'], Cart[i]['Price']))
	Amount = Items_List[Product]['Price'] * Quantity
	Total_Amount += Amount
	print("\nTotal Amount = ", Total_Amount)

# Function to take order from the customer
def OrderList():
	while (True):
		print("\nSelect an option: \n1. Add Item \n2.Exit \n")
		choice = int(input("Enter your option:"))
		if choice == 1:
			AddItem()
		elif choice == 2:
			quit()
		else:
			print("Enter valid number")

OrderList()
