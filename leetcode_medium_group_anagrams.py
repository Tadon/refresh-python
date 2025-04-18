'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.


An anagram is a string that contains the exact same characters as another string,
 but the order of the characters can be different.


 Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]


'''
#Sorted solution

'''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            if key in new_dict:
                new_dict[key].append(word)
            else:
                new_dict[key] = [word]
        return new_dict.values()
        '''

#Frequency array solution

class Solution(object):
    def groupAnagrams(self, strs):
        new_dict = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                letter_index = ord(letter) - ord('a')
                freq[letter_index] += 1
            key = tuple(freq)
            if key in new_dict:
                new_dict[key].append(word)
            else:
                new_dict[key] = [word]
        return new_dict.values()
                