from collections import Counter

def is_permutation(thing1, thing2):
    return Counter(thing1) == Counter(thing2)

print is_permutation("LMAO", "MALO")
