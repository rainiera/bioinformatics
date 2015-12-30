"""
Returns true if a list-like object, including strings, is a palindrome. Otherwise false.
"""

def isPalindrome(list):
    return list == list[::-1]

if __name__ == '__main__':
    # test 1
    expected = True
    actual = isPalindrome('racecar')
    print "TEST 1 isPalindrome('racecar')"
    print " expected: True, actual: " + str(actual)
    if (expected == actual):
        print " test passed"
    else:
        print " **FAILED**"

    print ""

    # test 2
    expected = False
    actual = isPalindrome('This is not a palindrome')
    print "TEST 2 isPalindrome('This is not a palindrome')"
    print " expected: False, actual: " + str(actual)
    if (expected == actual):
        print " test passed"
    else:
        print " **FAILED**"

    # test 3
    expected = False
    actual = isPalindrome([23, 48, "bats", 340923, 3.5, "The Smiths", [32, "singleton no more"]])
    print "TEST 2 isPalindrome([23, 48, \"bats\", 340923, 3.5, \"The Smiths\", [32, \"singleton no more\"]])"
    print " expected: False, actual: " + str(actual)
    if (expected == actual):
        print " test passed"
    else:
        print " **FAILED**"

    # test 4
    expected = True
    actual = isPalindrome([23, 48, "bats", 340923, 3.5, "The Smiths", [32, "singleton no more"],
                           [32, "singleton no more"], "The Smiths", 3.5, 340923, "bats", 48, 23])
    print "TEST 2 isPalindrome([23, 48, \"bats\", 340923, 3.5, \"The Smiths\", [32, \"singleton no more\"]," \
          "[32, \"singleton no more\"], \"The Smiths\", 3.5, 340923, \"bats\", 48, 23])"
    print " expected: True, actual: " + str(actual)
    if expected == actual:
        print " test passed"
    else:
        print " **FAILED**"