def count_vowels(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in string:
        if i in vowels:
            count += 1
    return count
print(count_vowels("Python Programming"))