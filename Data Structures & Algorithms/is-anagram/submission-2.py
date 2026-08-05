class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        nS = Counter(s)
        nT = Counter(t)
        if nS == nT:
            return True
        return False