#problem : https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


#Brute-force logic
from ctypes.wintypes import tagRECT


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for ind,i in enumerate(nums):
            for ind1, j in enumerate(nums):
                if ind==ind1:
                    continue
                else:
                    if i+j==target:
                        return [ind,ind1]

#Optmized logic

#logic a+b = target
#    then target-a=b
#    also target-b=a

class Solution_Op(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict={}
        for i in range(0,len(nums)):
            if target-nums[i] in sum_dict:
                return [sum_dict[target-nums[i]],i]
            else:
                sum_dict[nums[i]]=i



  

        