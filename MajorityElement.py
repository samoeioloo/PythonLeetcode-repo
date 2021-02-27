# question:
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #hashmap approach:
        # We know that the majority element occurs more than n/2 times, and a HashMap allows            us to count element occurrences efficiently.
        # We can use a HashMap that maps elements to counts in order to count occurrences in            linear time by looping over nums. Then, we simply return the key with maximum value
        #Time complexity : O(n) 
        # We iterate over nums once and make a constant time HashMap insertion on each                      iteration. Therefore, the algorithm runs in O(n) time.
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
        
        
        #brute force approach -> takes wayyyy too long
        # for x in nums:
        #     if nums.count(x) > len(nums)/2:
        #         return x
        