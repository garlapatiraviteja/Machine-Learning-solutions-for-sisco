s = raw_input()
k = input()

for i in range(len(s) / k):
    x = ''
    for c in s[i * k : (i + 1) * k]:
        if c in x:
            continue
        x += c
    print x

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)