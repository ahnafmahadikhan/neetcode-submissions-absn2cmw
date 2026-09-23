class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        maxx = 0x7FFFFFFF

        while b:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        if a <= maxx:
            return a
        else:
            return ~(a ^ mask)