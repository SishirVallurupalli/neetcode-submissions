class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestString = ""
        for i in range(len(s)):
            l = i
            r = i
            while r >= 0 and l >= 0 and l < len(s) and r < len(s):
                sub = s[l:r + 1]
                # print(sub)
                if s[l] == s[r]:
                    l -= 1
                    r+= 1
                else:
                    break
                if len(sub) > len(longestString):
                    longestString = sub
            l = i
            r = i + 1
            while r >= 0 and l >= 0 and l < len(s) and r < len(s):
                sub = s[l:r + 1]
                # print(sub)
                if s[l] == s[r]:
                    l -= 1
                    r+= 1
                else:
                    break
                if len(sub) > len(longestString):
                    longestString = sub
        return longestString