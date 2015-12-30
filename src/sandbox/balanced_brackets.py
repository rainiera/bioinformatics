'''
Given a string made up of the characters '(', '[', '{', '}', ']', ')', returns
whether the string has balanced brackets or not,

e.g., '({}[])()' is balanced; '(({]' is not balanced.
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
            # if the last item of the stack (all left characters)
            #  does NOT map to the character we're looking at; return false
            if not stack or stack.pop() != right_to_left[char]:
                return False

    # if there are remaining items in the stack, you have
    #  extra left parens left with nothing to close them with; return false
    if stack:
        return False

    # finished iterating through the string
    #  and the stack ended up empty; return true
    return True

if __name__ == '__main__':
    # some tests
    a = '({}[])()'
    b = '(({]'
    c = '((((([][][][]))))){}{}()'
    d = '{}(})()})()()}()(][]][][][}}}}[[[{{}'
    e = '{[}]'
    if bracketsAreBalanced(a):
        print 'Test a passed, bracketsAreBalanced(' + '\'' + a + '\'' + ')'
    if not bracketsAreBalanced(b):
        print 'Test b passed, bracketsAreBalanced(' + '\'' + b + '\'' + ')'
    if bracketsAreBalanced(c):
        print 'Test c passed, bracketsAreBalanced(' + '\'' + c + '\'' + ')'
    if not bracketsAreBalanced(d):
        print 'Test d passed, bracketsAreBalanced(' + '\'' + d + '\'' + ')'
    if not bracketsAreBalanced(e):
        print 'Test e passed, bracketsAreBalanced(' + '\'' + e + '\'' + ')'
