n=int(input())
print()
def twoStrings(s1,s2):
    if set(s1)&set(s2):
        return "FOUND"
    else:
        return "NOT FOUND"
for _ in range(n):
    s1=input()
    s2=input()
    print("Common substring",twoStrings(s1,s2))
    print()
