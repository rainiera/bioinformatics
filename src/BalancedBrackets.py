__author__ = 'rainierababao'

'''
Given a string made up of the characters '(', '[', '{', '}', ']', ')', returns
whether the string has balanced brackets or not,

e.g., '({}[])()' is balanced; '(({]' is not balanced.


Apparently this is also a common interview question.
Inspired by this set of pretty good videos:
http://smithamilli.com/blog/most-common-interview-questions/
'''


left_set = {'(', '{', '['}
right_set = {')', '}', ']'}
right_to_left = {
    ')': '(',
    '}': '{',
    ']': '['
}

def bracketsAreBalanced(input_str):
    stack = []
    for char in input_str:
        if char in left_set:
            stack.append(char)
        elif char in right_set:
            if not stack or stack.pop() != right_to_left[char]:
                return False
    if stack:
        return False
    return True

if __name__ == '__main__':
    # some tests
    a = '({}[])()'
    b = '(({]'
    c = '((((([][][][]))))){}{}()'
    d = '{}(})()})()()}()(][]][][][}}}}[[[{{}'
    if bracketsAreBalanced(a) == True:
        print 'Test a passed, bracketsAreBalanced(' + '\'' + a + '\'' + ')'
    if bracketsAreBalanced(b) == False:
        print 'Test b passed, bracketsAreBalanced(' + '\'' + b + '\'' + ')'
    if bracketsAreBalanced(c) == True:
        print 'Test c passed, bracketsAreBalanced(' + '\'' + c + '\'' + ')'
    if bracketsAreBalanced(d) == False:
        print 'Test d passed, bracketsAreBalanced(' + '\'' + d + '\'' + ')'