def count_char_in_string(s, char):
    count = 0
    for letter in s:
        if letter == char:
            count += 1
    return count
s, char = map(str, input('Enter string and character: ').split(' '))
print(count_char_in_string(s, char))