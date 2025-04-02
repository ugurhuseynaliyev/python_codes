def split_three_digit_number(number):
    digits = ''
    if number >= 100 and number <= 999:
        while number > 0:
            digit = number % 10
            digits += str(digit)
            number //= 10
    digits = digits[::-1]
    return f'({', '.join(map(str, digits))})'
    
print(split_three_digit_number(569))