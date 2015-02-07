__author__ = 'rainierababao'

"""
Returns the Hamming Distance of two strings, defined as the minimum number of character
changes required of one string to make it identical to another string. Is case-sensitive.
"""

"""
preconditions:
    neither parameter may be null
    strings must be of equal length
"""

def hammingDistance(str1, str2):
    if str1 is None or str2 is None or len(str1) != len(str2):
        raise Exception("Neither parameter may be null, strings must be equal length")

    diff = 0;
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            diff += 1
    return diff

if __name__ == '__main__':
    # test 1
    expected = 1
    actual = hammingDistance('test', 'rest')
    print "TEST 1 is hammingDistance('test', 'rest')"
    print " expected: 1, actual: " + str(actual)
    if (expected == actual):
        print " test passed"
    else:
        print " **FAILED**"
    print ""

    # test 2
    expected = 10
    actual = hammingDistance('AaAaAaAaAa', 'aAaAaAaAaA')
    print "TEST 2 is hammingDistance('AaAaAaAaAa', 'aAaAaAaAaA')"
    print " expected: 10, actual: " + str(actual)
    if (expected == actual):
        print " test passed"
    else:
        print " **FAILED**"
    print ""