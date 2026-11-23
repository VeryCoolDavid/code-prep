class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        length=0
        my_set=set()
        for r,c in enumerate(s):
            while c in my_set:
                my_set.remove(s[l])
                l+=1
            my_set.add(c)
            length=max(r-l+1,length)
        return length 