'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

'''

'''
#O(nlogn) very ineffecient
class Solution(object):
    def topKFrequent(self, nums, k):
        empty_dict = {}
        for i in nums:
            if i in empty_dict:
                empty_dict[i] += 1
            else:
                empty_dict[i] = 1
        empty_dict = {k: v for k, v in sorted(empty_dict.items(), key=lambda item: item[1], reverse = True)}
        empty_array = []
        for i in empty_dict:
            empty_array.append(i)
        final_array = []
        for i in range(k):
            final_array.append(empty_array[i])
        return final_array'''
#O(n) solution
class Solution(object):
    def topKFrequent(self, nums, k):
        empty_dict = {}
        for i in nums:
            if i in empty_dict:
                empty_dict[i] += 1
            else:
                empty_dict[i] = 1
        bucket = [[]for i in range(len(nums ) + 1)]
        for number, frequency in empty_dict.items():
            bucket[frequency].append(number)
        bucket.reverse()
        final_array = []
        x = 0
        for i in bucket:
            for j in i:
                final_array.append(j)
                x += 1
                if x == k:
                    return final_array
s = Solution()
print(s.topKFrequent([4, 1, 2, 2, 3, 4, 4, 1, 2, 3, 3, 3], 2))
# 3 should be first (4 times), then 4 (3 times), then 2 (3 times), then 1 (2 times)

print(s.topKFrequent([9, 8, 7, 9, 8, 7, 9, 8, 7, 7, 7], 3))
# 7 appears 5 times, 8 appears 3 times, 9 appears 3 times

print(s.topKFrequent([5, 5, 6, 6, 6, 7], 1))
# 6 appears 3 times

print(s.topKFrequent([1, 2, 3, 4, 5], 5))
# Each number appears once, order by value should be arbitrary because all frequencies are the same

print(s.topKFrequent([100, 200, 100, 300, 200, 100, 300, 300, 300], 2))
# 300 appears 4 times, 100 appears 3 times, 200 appears 2 times