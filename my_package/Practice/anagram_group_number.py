def find_anagram_group_number(words):
    anagram_sets = set()
    
    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_sets.add(sorted_word)
    
    return len(anagram_sets)

print(find_anagram_group_number(["listen", "silent", "enlist", "rat", "tar", "art", "cat", "tac", "arm"]))