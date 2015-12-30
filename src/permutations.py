from itertools import permutations

plist = list(permutations(range(1,7)))
print len(plist)

for permutation in plist:
    permutation = map(str, list(permutation))
    print ' '.join(permutation)
