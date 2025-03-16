def check_number_type(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

num = int(input('Enter number: '))
print(check_number_type(num))