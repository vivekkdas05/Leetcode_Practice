# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Date: Oct 23, 2025

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j] 
        
