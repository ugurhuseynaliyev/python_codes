def prime_numbers_between_ranges(start, end):
    prime_number_count = 0
    for num in range(start, end + 1):
        if isPrimeNumber(num):
            prime_number_count += 1
    return prime_number_count

def isPrimeNumber(num):
    count = 0
    if num < 2:
        return False
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True
    
start, end = map(int, input('Enter start and end: ').split(' '))
print(prime_numbers_between_ranges(start, end))