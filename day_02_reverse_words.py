'''
    Write a function reverse_words(s) that takes a string s and returns the string with the order of words reversed.

    Rules:

        Words are separated by spaces.

        Keep the words themselves the same (don't reverse letters inside the words).

        No need to handle extra spaces or punctuation for now—keep it simple.
'''

def reverse_words(s):
    s += ' '                                 #adding space at the end of string to make it easier to add word at end of sentence, because i use an empty space to trigger adding a word to a word list
    word_list = []                           #converting a string to a list of words, so i can use the built in reversed function to rebuild the sentence later in the logic
    word = ''                                #string variable used to create individual words from string s
    reversed_sentence = ''                   #sentence in reversed, the required solution to the problem
    for letters in s:                        #creating the list of words made from string s by iterating through each character (including empty spaces) within the given string s    
        if letters != ' ':                   #basically checking to see if the character isn't an empty space
            word += letters                  #adding the iterating "letters" into the variable "word" to create the individual word
        else:                                #basically, if the character is an empty space
            word_list.append(word)           #since having an empty space is the end of a word, i am appending the completed word into the word list, converting the string into a list of words
            word = ''                        #resetting the word variable to an empty string, so that after each space/empty character, the next word can be built
    
    for i in reversed(word_list):            #using reversed method to reverse the list of words in word_list, making it possible to re create the sentence in reverse
        reversed_sentence += i               #adding each completed word to the new, reversed string
        if i != word_list[0]:                #basically checking to see if the current word is == to the first word in the original sentence, so i dont add an unnecessary space to the end of a sentence
            reversed_sentence += " "         #adding a space between words that aren't the final words in a sentence
    return reversed_sentence                 #returning the reversed string, as per the question requests
       
        
    

print(reverse_words("hello world"))        # world hello
print(reverse_words("Python is awesome"))  # awesome is Python
print(reverse_words(""))                   # (empty string)