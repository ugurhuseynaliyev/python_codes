def prime_number(number):
    count = 0
    if number > 1:
        for i in range(1, number+1):
            if number % i == 0:
                count += 1
    if count > 2:
        return False
    else:
        return True
print(prime_number(10))
