class Solution:

    def encode(self, strs: str) -> str:
        s = ''
        for i in strs:
            l = str(len(i))
            word = l + '#' + i
            s += word
        print(s)
        return s
    def decode(self, s: str):
        return_array = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            return_array.append(word)
            i = j + 1 + length
        return return_array
