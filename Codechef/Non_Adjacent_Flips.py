// Problem Link: https://www.codechef.com/START33B/problems/NONADJFLIP/

t=int(input())
for z in range(t):
    n=int(input())
    s=input()
    zero=0
    one=0
    for i in range(n):
        if s[i]=='0':
            zero+=1 
    if zero==n:
        print('0')
        continue
    j=1 
    
    for i in range(n-1):
        if s[i]=='1' and s[j]=='1':
            one=1
            break
        j+=1 
    if one==0:
        print('1') 
    else:
        print('2')
