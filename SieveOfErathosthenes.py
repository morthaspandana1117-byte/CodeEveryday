class Solution:
    def sieve(self, n:int):
        prime = [True]*(n+1)
        prime[0]=prime[1]=False
        
        p=2
        while p*p <=n:
            if prime[p]:
                for j in range(p*p,n+1,p):
                    prime[j]=False
            p+=1
        return (i for i in range(2,n+1) if prime[i])


if __name__ == "__main__":
    n = int(input("Enter a number:"))
    sol = Solution()
    primes = sol.sieve(n)
    print(*primes)

# Code Reusability:

# You can write functions or classes in a file and reuse them elsewhere without running the script’s main logic.
# Testing or Running as Script:
# You can add test cases or example runs in the block, which will only execute when you directly run the file.
# Prevents Unwanted Execution:
# If another file imports this file, the code inside this block won't run, preventing side effects.        