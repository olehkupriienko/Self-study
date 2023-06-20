class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False
