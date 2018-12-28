
import itertools

x = raw_input()

for k, g in itertools.groupby(x):
    print (len(list(g)), int(k)),