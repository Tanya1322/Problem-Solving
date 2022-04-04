// Problem Link: https://leetcode.com/problems/maximum-average-subarray-i/
  
  import sys
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1 and k==1:
            return nums[0]
        max_average=-sys.maxsize-1
        ws=0
        curr_sum=0
        curr_average=0
        for we in range(0,len(nums)):
            if we-ws+1>k:
                curr_average=curr_sum/k
                max_average=max(max_average,curr_average)
                curr_sum-=nums[ws]
                ws+=1
            curr_sum+=nums[we]
        curr_average=curr_sum/k
        max_average=max(max_average,curr_average)
        return max_average
