class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = {}
        tD = {}
        for c in s:
            sD[c] = sD.get(c, 0) + 1
        for c in t:
            tD[c] = tD.get(c, 0) +  1
        return sD == tD        