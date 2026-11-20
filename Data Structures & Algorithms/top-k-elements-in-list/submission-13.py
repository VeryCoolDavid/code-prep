class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap=[]
        for n in count.keys():
            heapq.heappush(heap,(count[n],n))
            if len(heap)>k:
                heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        