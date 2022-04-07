// Problem Link: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#
    
    import sys

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        ws=0
        min_diff=sys.maxsize
        curr_diff=0
        for we in range(len(A)):
            curr_diff=A[we]-A[ws]
            if we-ws+1>=M:
                min_diff=min(min_diff,curr_diff)
                ws+=1
        return min_diff
