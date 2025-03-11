def inventorySystemSimulator():
    item_name1, item_name2, item_name3 = input('Enter names of items: ').split()
    quantity1, quantity2, quantity3 = map(int, input('Enter quantities of items: ').split())

    while True:
        item_sell = input('Enter item name to sell or e (exit): ')
        item_quantity = int(input(f'Enter quantity of {item_sell}: '))

        if item_sell == item_name1:
            if quantity1 < item_quantity:
                print(f'Insufficient stock! You have only {quantity1} for {item_sell}')
            else:
                quantity1 -= item_quantity
                print(f'Sold {item_quantity} of {item_sell}. In stock {quantity1}')
        elif item_sell == item_name2:
            if quantity2 < item_quantity:
                print(f'Insufficient stock! You have only {quantity2} for {item_sell}')
            else:
                quantity2 -= item_quantity
                print(f'Sold {item_quantity} of {item_sell}. In stock {quantity2}')
        elif item_sell == item_name3:
            if quantity3 < item_quantity:
                print(f'Insufficient stock! You have only {quantity3} for {item_sell}')
            else:
                quantity3 -= item_quantity
                print(f'Sold {item_quantity} of {item_sell}. In stock {quantity3}')
inventorySystemSimulator()