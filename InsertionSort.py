class Solution:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(1,n):
            key = arr[i]
            j=i-1
        
            while j>=0 and arr[j]>key :
              arr[j+1]=arr[j]
              j=j-1
            arr[j+1]=key
        
        return

arr = [4,1,7,3,9]
sol = Solution()
sol.insertionSort(arr)
print("Array after sorting:",arr)