class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp= set()
        for num in nums:
            if num not in tmp:
                tmp.add(num)
        return len(nums)!=len(tmp)
                