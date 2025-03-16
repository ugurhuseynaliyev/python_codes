def unique_char_strings_average(sentence):
    word_arr = sentence.split(' ')
    result = []

    for string in word_arr:
        if len(string) == len(set(string)):
            result.append(string[::-1])
        else:
            result.append(string)
    return ' '.join(result)
print(unique_char_strings_average('hello world abc defg unique'))