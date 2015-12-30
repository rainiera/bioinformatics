inp = ""
a = map(lambda x: int(x), inp.split(" "))
print len(a)

def count_swaps(a):
    swaps, i, j = 0, 0, 0
    for i in range(1, len(a)-1):
        j = i
        while j >= 0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            swaps += 1
            j -= 1
    return swaps

class Bit:
    def __init__(self, n):
        sz = 1
        while n > sz:
            sz *= 2
        self.size =sz
        self.data = [0]*sz
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

def inversions(A):
    res = 0
    bit = Bit(max(A)+1)
    for i, v in enumerate(A):
        res += i - bit.sum(v)
        bit.add(v, 1)
    return res

print inversions(a)
