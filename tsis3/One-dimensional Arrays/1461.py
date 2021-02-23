def destroy(a, i, counter):
    if i+1 < len(a) and a[i]==a[i+1]:
        counter+=1
        return destroy(a, i+1, counter)
    else:
        return counter, i

a = list(map(int, input().split()))
cnt = 0
i = 0
while i < len(a):
    counter = 1
    ans = destroy(a, i, counter)
    if ans[0]>=3:
        cnt+=ans[0]
        del a[i:ans[1]+1]
        i=0
    else:
        i+=1
print(cnt)