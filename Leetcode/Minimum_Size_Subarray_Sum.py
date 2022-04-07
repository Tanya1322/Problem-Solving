// Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/
    
import sys
    class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=sys.maxsize
        ws=0
        curr_sum=0
        for we in range(0,len(nums)):
            curr_sum+=nums[we]
            if curr_sum>=target:
                min_length=min(min_length,we-ws+1)
                while curr_sum>=target:
                    curr_sum-=nums[ws]
                    ws+=1
                    if curr_sum>=target:
                        min_length=min(min_length,we-ws+1)
        if min_length==sys.maxsize:
            return 0
        else:
            return min_length
