class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        anagram = dict()
        for i in s:
            if i in anagram:
                anagram[i] = anagram.get(i) + 1
            else:
                anagram[i] = 1
        
        for i in t:
            if i not in anagram:
                return False
            else:
                anagram[i] = anagram.get(i) - 1

        for value in anagram.values():
            if value > 0:
                return False
        
        return True
