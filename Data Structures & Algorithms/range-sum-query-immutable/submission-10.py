class NumArray:

    def __init__(self, nums: List[int]):
        self.postfix=[0]* len(nums)
        self.total=0
        for i in range(len(nums)-1,-1,-1):
            self.total+=nums[i]
            self.postfix[i]=self.total

    def sumRange(self, left: int, right: int) -> int:
        left = self.postfix[left]
        right = self.postfix[right + 1] if right + 1 < len(self.postfix) else 0
        return left - right


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)