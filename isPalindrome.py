__author__ = 'rainierababao'

"""checks if a string is a palindrome"""

def isPalindrome(word):
    return word == word[::-1]

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