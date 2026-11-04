class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range (len(arr)): 
            temp=0
            if  i != len(arr)-1: 
              for j in range(i+1,len(arr)):
                  temp=max(temp,arr[j])
              arr[i]=temp
            else:arr[i]=-1
        return arr