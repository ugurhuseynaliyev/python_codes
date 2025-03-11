operator = input('Enter operator: ')
num1 = float(input('Number 1: '))
num2 = float(input('Number 2: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('Can not divide by zero')