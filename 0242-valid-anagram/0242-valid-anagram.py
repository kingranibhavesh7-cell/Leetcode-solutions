class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        lst = [0] * 26

        for ch in s:
            lst[ord(ch) - 97] += 1
        for ch in t:
            lst[ord(ch) - 97] -= 1

        for count in lst:
            if count != 0:
                return False

        return True
        