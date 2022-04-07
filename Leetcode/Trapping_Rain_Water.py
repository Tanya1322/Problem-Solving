// Problem link: https://leetcode.com/problems/trapping-rain-water/
    
    class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[-1]
        ngel=[]
        nger=[]
        water=0
        for i in range(len(height)):
            if stack[-1]<height[i]:
                stack.pop()
                stack.append(height[i])
            ngel.append(stack[-1]-height[i])
        while len(stack)!=0:
            stack.pop()
        stack.append(-1)
        for i in range(len(height)-1,-1,-1):
            if stack[-1]<height[i]:
                stack.pop()
                stack.append(height[i])
            nger.append(stack[-1]-height[i])
        nger.reverse()
        for i in range(len(height)):
            water+=min(ngel[i],nger[i])
        return water
