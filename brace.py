def isBalanced(s):
    stack = list(s)
    opens = ['(','[','{']
    closes = [')',']','}']
    for index, brace in enumerate(s):
        if brace in opens:
            if closes[opens.index(brace)] in stack:
                stack.remove(brace)
                stack.remove(closes[opens.index(brace)])
    return len(stack) == 0

print(isBalanced('()()()(())'))
