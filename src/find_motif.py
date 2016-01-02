def get_substr_indices(s, t):
    starts = []
    window = len(t)
    for i in range(len(s)-window):
        if s[i:i+window] == t:
            starts.append(i+1)
    return starts

s = raw_input()
t = "TGCAGTATG"
print " ".join(map(lambda x: str(x), get_substr_indices(s, t)))
