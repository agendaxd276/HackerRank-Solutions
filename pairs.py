def pairs(k, arr):
    arr = set(arr)
    return sum(1 for i in arr if i+k in arr)
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print()
print("Pairs: ",pairs(k, arr))
