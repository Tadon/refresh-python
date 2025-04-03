#Write a function has_unique_characters(s) that returns True if the string s has all unique characters (no repeats), and False otherwise.#

def has_unique_characters(string):
    character_checker = []
    for character in string:
        if character not in character_checker:
            character_checker.append(character)
        else:
            return False
    return True

print(has_unique_characters("hello"))
print(has_unique_characters("world") )
print(has_unique_characters(""))
print(has_unique_characters("a"))