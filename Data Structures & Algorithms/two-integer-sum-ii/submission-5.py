class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        if not numbers:
            return res
        l,r = 0,len(numbers)-1
        while l<r:
            twoSum= numbers[l] + numbers[r]
            if twoSum<target:
                    l+=1
            elif twoSum>target:
                    r-=1
            else:
                res.append(l+1)
                res.append(r+1)
                l+=1
                r-=1
                while l < r and numbers[l]==numbers[l-1]:
                    l+=1
        return res