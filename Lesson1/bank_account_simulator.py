init_balance = int(input('Enter initial balance: '))

while True:
    choice = input('Deposit (d) or Withdraw (w)? => ')
    amount = int(input('Enter amount: '))

    if choice == 'Deposit' or choice == 'd':
        init_balance += amount
        print(f'You deposited {amount} money. Your balance: {init_balance}')
    elif choice == 'Withdraw' or choice == 'w':
        if amount > init_balance:
            print(f'There are not enough balance in your account. Your balance: {init_balance}')
        else:
            init_balance -= amount
            print(f'You withdrawed {amount} money. Your balance: {init_balance}')
    else:
        print('Invalid input!')