def find_longest_word(words):
    longest_word = words[0]
    for i in range(1, len(words)):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]
    return longest_word
print(find_longest_word(["a", "abcd", "abc"]))