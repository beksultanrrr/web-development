#runner - up
n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
res = -100500
for i in arr:
    if i != mx and i > res: res = i
if res == -100500: print('')
else: print(res)