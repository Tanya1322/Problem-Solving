// Problem Link: https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap=dict()
        ws=0
        res=[]
        for we in range(9,len(s)):
            hashmap[s[ws:we+1]]=hashmap.get(s[ws:we+1],0)+1
            ws+=1
        for key,value in hashmap.items():
            if value>1:
                res.append(key)
        return res
