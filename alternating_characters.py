n=int(input())
print()
def alternatingCharacters(s):
    count=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
    return count
for _ in range(n):
    s=input()
    print("Deletions: ",alternatingCharacters(s))
    print()
