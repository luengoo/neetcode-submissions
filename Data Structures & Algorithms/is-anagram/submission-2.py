class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = []
        for letter in s:
            letters.append(letter)
        for letter in t:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        if len(letters) != 0:
            return False
        return True