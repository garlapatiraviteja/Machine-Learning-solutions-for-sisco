S = raw_input()
l = len(S)
stu= 0
kev = 0

for i in range(l):
    if S[i] in ('A', 'E', 'I', 'O', 'U'):
        kev += l - i
    else:
        stu += l - i

if kev > stu:
    print 'Kevin', kev
elif stu > kev:
    print 'Stuart', stu
else:
    print 'Draw'    
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)