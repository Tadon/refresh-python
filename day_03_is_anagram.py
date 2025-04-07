'''
Problem: Write is_anagram(s1, s2) to check if two strings are anagrams.

    Ignore spaces.

    Ignore casing.

    Return True or False.
'''

def is_anagram(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ",""))


print(is_anagram("listen", "silent"))   # True
print(is_anagram("Hello", "Olelh"))      # True
print(is_anagram("test", "taste"))       # False
print(is_anagram("a gentleman", "elegant man"))  # True