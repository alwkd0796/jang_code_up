a, b=input().split()

a=bool(int(a))
b=bool(int(b))

print(((not(a)) and b) or (a and (not(b))))