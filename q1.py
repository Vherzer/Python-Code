def anagram_validator(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


s1 = "listen"
s2 = "silent"
anagram_validator(s1, s2)