'''
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

'''
O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_num = None
        second_num = None 
        for i in range(len(nums)):
            
            if target-nums[i] in nums[i+1:]:
                first_num = i
            if first_num != None and nums[first_num] + nums[i] == target:
                second_num = i
                
                
                

        return first_num, second_num
        '''

#correct, O(n) time solution:
class Solution(object):
    def twoSum(self, nums, target):
        
        empty_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in empty_dict:
                return empty_dict[target-nums[i]], i
            else:
                empty_dict[nums[i]] = i
        return "Error"

print(Solution().twoSum([2, 7, 11, 15], 9))        # [0, 1]
print(Solution().twoSum([3, 2, 4], 6))             # [1, 2]
print(Solution().twoSum([3, 3], 6))                # [0, 1]
print(Solution().twoSum([1, 5, 3, 6], 9))          # [1, 3]
print(Solution().twoSum([1, 2, 3, 4, 5, 6], 7))    # [0, 5] or [1, 4] depending on how you handle it
print(Solution().twoSum([0, 4, 3, 0], 0))          # [0, 3]
print(Solution().twoSum([-3, 4, 3, 90], 0))        # [0, 2]
print(Solution().twoSum([1, 2, 5, 6], 10))         # "Error"
print(Solution().twoSum([2, 5, 5, 11], 10))        # [1, 2]
print(Solution().twoSum([5, 75, 25], 100))         # [1, 2]