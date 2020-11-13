def is_a_match(o,c):
    if o=="(" and c==")":
        return True
    elif o=="{" and c=="}":
        return True
    elif o=="[" and c=="]":
        return True
    else:
        return False

def is_balanced(string):
    balanced=True
    stack=[]
    for letter in string:
        if letter in "({[":
            stack.append(letter)
        else:
            if not stack:
                balanced=False
            else:
                popped = stack.pop()
                if not is_a_match(popped, letter):
                    balanced=False
    if not stack and balanced:
        return True
    else:
        return False

print(is_balanced("[{}}]()"))
