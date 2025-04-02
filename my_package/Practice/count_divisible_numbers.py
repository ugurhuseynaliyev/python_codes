def count_divisible_numbers(lst, d):
    count = 0
    for num in lst:
        if num % d == 0:
            count += 1
    return count
print(count_divisible_numbers([3, 7, 11, 14, 18], 2))