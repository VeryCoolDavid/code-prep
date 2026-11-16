import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    result=[]
    for num in nums:
        pair = (-num, num)
        heapq.heappush(result, pair)
    tmp=[]
    while result:
        pair = heapq.heappop(result)
        original= pair[1]
        tmp.append(original)
    return tmp




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
