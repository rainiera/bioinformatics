__author__ = 'rainierababao'

import random

def fill(result, length):
    for i in range(1, length):
        result = result + random.choice(seq)
    return result

if __name__ == "__main__":
    seq = ["A", "C", "G", "T"]
    result = ""
    print fill(result, 100)
    print fill(result, 50)
    print fill(result, 25)
