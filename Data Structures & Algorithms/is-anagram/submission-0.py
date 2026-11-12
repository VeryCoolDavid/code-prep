class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s1=sorted(s)
            t1=sorted(t)
            return s1==t1
        return False