// Problem Link: https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/?page=1&category[]=prefix-sum&sortBy=submissions#
    
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        total=sum(A)
        prefix_sum=A[0]
        rsum=total-prefix_sum
        if 0==rsum:
            return 1
        for i in range(1,N):
            prefix_sum+=A[i]
            lsum=prefix_sum-A[i]
            rsum=total-prefix_sum
            if lsum==rsum:
                return i+1
        return -1
