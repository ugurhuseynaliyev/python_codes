def inventorySystem():
    item_name1, item_name2, item_name3 = input('Enter item names: ').split()
    quantity1, quantity2, quantity3 = map(int, input('Enter quantities: ').split())
    while True:
        selling_item = input('Enter item name to sell: ')
        quantity = int(input(f'Enter quantity of {selling_item}: '))

        if selling_item == item_name1:
            if quantity1 < quantity:
                print(f'Insufficient stock. You have only {quantity1} for {selling_item}')
            else:
                quantity1 -= quantity
                print(f'Sold {quantity} of {selling_item}. In stock {quantity1}')
        if selling_item == item_name2:
            if quantity2 < quantity:
                print(f'Insufficient stock. You have only {quantity2} for {selling_item}')
            else:
                quantity2 -= quantity
                print(f'Sold {quantity} of {selling_item}. In stock {quantity2}')
        if selling_item == item_name3:
            if quantity3 < quantity:
                print(f'Insufficient stock. You have only {quantity3} for {selling_item}')
            else:
                quantity3 -= quantity
                print(f'Sold {quantity} of {selling_item}. In stock {quantity3}')

inventorySystem()