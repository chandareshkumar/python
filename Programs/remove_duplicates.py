# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Logic reversed the list
# if current element is same as next element replace current element

# why to reverse the list and do this logic?

#     for ex : nums = [1, 1, 2, 3, 3]

#     If you remove nums[0] (the first 1), the second 1 shifts to index 0. 
#     But the loop moves to the next index (ind = 1), so the second 1 is skipped entirely. 
#     This is why modifying the list in place while looping forward can cause issues.


class Solution(object):
    def removeDuplicates(self, nums):
        for ind in range(len(nums)-1,0,-1):
            if nums[ind]==nums[ind-1]:
                nums.pop(ind)
        return len(nums)