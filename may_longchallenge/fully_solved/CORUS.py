# cook your dish here
for _ in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    count={}
    for i in s:
        if i in count:
            count[i]+=1 
        else:
            count[i]=1
    for i in range(q):
        val=0
        c=int(input())
        for key in count:
            if count[key]>c:
                val+=(count[key]-c)
        print(val)
