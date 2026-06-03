class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        x = 0
        while x < len(s):
            j = s.find("#", x)
            length = int(s[x:j])
            result.append(s[j + 1 : j + 1 + length])
            x = j + 1 + length
        return result