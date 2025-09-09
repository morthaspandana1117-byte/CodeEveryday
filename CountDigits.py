class Solution:
    def countDigits(self, n):
      count=0
      while(n>0):
        count+=1
        n//=10
      return count    

sol = Solution()
print(sol.countDigits(47574))      