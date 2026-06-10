class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_open = "([{"
        valid_close = "])}"
        open_dict = {
            "[":"]",
            "(":")",
            "{":"}"
        }
        for letter in s:
            if letter in valid_open:
                stack.append(letter)
            elif letter in valid_close:
                if stack:
                    check = stack.pop()
                    if open_dict[check] == letter:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False