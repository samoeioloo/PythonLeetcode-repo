class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        try:
            for i in range(len(s)):
                value = romans[s[i]] #value placeholder
                #if next place holder is larger the value is negative ie minus one if before, plus one if after
                if i + 1 < len(s) and romans[s[i+1]] > value:
                    sum -= value 
                else:
                    sum += value
            return sum
        except KeyError:
            raise ValueError, 'input is not a valid Roman numeral: %s' % s
    