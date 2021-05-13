class Solution:
    def isHappy(self, n: int) -> bool:
        it = set([n])
        while n != 1:
            next_n = 0
            while n != 0:
                next_n += (n % 10)**2
                n = (n - n % 10) / 10
            n = int(next_n)
            if n in it:
                return False
            else:
                it.add(n)
        return True