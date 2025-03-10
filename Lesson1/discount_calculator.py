total_amount = int(input('Enter total purchase amount: '))

def discountCalculator(total_amount):
    if total_amount >= 1000:
        discount = total_amount * 0.2
        total_amount -= discount
        print(f'Dicount: {discount}, Total payment: {total_amount}')
    elif total_amount >= 500:
        discount = total_amount * 0.1
        total_amount -= discount
        print(f'Dicount: {discount}, Total payment: {total_amount}')
    else:
        print("Discount didn't applied for you")
    
discountCalculator(total_amount)