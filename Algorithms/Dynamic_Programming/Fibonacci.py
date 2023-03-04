# Implement Fibonacci sequence using memoization.

class dynamic:
    def memoFib(self, number):
        return self.mFib(number)

    def mFib(self, n, memo = {}): # memo is working as cache for storing values.
        if n < 2:
            return n

        else:
            if n in memo:
                return memo[n]
            else:
                result = self.mFib(n - 1) + self.mFib(n - 2)
                memo[n] = result
                return result

    def normal_fib(self, n): # Bottom-up Solution.
        ans = [0, 1]
        if n < 2:
            return n
        for i in range(2, n + 1):
            ans.append(ans[i-1] + ans[i-2])

        return ans.pop() 

m = dynamic()

print(m.memoFib(9))
print(m.normal_fib(9))