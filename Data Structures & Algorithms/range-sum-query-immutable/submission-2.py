class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        self.total=0
        for num in nums:
            self.total+=num
            self.prefix.append(self.total)

    def sumRange(self, left: int, right: int) -> int:
        right=self.prefix[right]
        left=self.prefix[left-1] if left > 0 else 0
        return right-left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)