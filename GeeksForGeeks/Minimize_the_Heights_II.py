// Problem Link: https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
    
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        maxa=arr[n-1]
        mina=arr[0]
        res=maxa-mina
        for i in range(1,n):
            maxa=max(arr[n-1]-k,arr[i-1]+k)
            mina=min(arr[0]+k,arr[i]-k)
            if mina<0:
                continue
            res=min(res,maxa-mina)
        return res
