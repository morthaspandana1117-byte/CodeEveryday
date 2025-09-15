class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        for i in range(0,n//2):
                arr[i] ,arr[n-1-i] = arr[n-1-i],arr[i]
        return arr

arr = [3,4,7,2,9]
sol = Solution()
sol.reverseArray(arr)
print("Reverse Array:",arr)