
(a,b) = map(int, raw_input().split())

arr = map(int, raw_input().split())
assert len(arr) == a

X = set(map(int, raw_input().split()))
assert len(X) == b

Y= set(map(int, raw_input().split()))
assert len(Y) == b

happy= 0

for i in arr:
    if i in X:
        happy += 1
    elif i in Y:
        happy -= 1

print happy
