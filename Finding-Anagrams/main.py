def find_palindrome(word):
    reversed_word = "".join(reversed(word))
    return word == reversed_word

# print(find_palindrome("racecar"))


def find_anagram(word1,word2):
    return sorted(word1) == sorted(word2)
        
# print(find_anagram("angel","glean"))
