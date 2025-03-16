def unique_char_strings_average(strings_list):
    unique_strings = []
    total_length = 0
    for string in strings_list:
        if len(string) == len(set(string)):
            unique_strings.append(string)
    for el in unique_strings:
        total_length += len(el)
    average = total_length // len(unique_strings)
    return average
print(unique_char_strings_average(["apple", "orange", "abc", "hello", "world", "xyz"]))