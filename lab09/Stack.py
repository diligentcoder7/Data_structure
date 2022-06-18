def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0:
        return print(stack[-1])
    else:
        print("Stack Empty")

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item
    else:
        print("Stack Empty")

def duplicate():
    if len(stack) != 0:
        a = stack[-1]
        stack.append(a)

def upRotate(n):
    if n <= len(stack):
        top = stack[-1]
        tmp = stack[-n:-1]
        del stack[-n:]
        stack.extend(top)
        stack.extend(tmp)
    else:
        return 0

def downRotate(n):
    if n <= len(stack):
        tmp = stack[-(n-1):]
        bottom = stack[-n]
        del stack[-n:]
        stack.extend(tmp)
        stack.extend(bottom)
    else:
        return 0

def PRINT():
    for i in range(len(stack)):
        print(stack[len(stack)-i-1], end='')
    print()

stack = []

while True:
    a = list(input())
    if a == ['P', 'O', 'P']:
        pop()
    elif a[:4] == ['P', 'U', 'S', 'H']:
        push(a[5])
    elif a[:5] == ['P', 'R', 'I', 'N', 'T']:
        PRINT()
    elif a[:3] == ['U', 'p', 'R']:
        upRotate(int(a[4]))
    elif a[:5] == ['D', 'o', 'w', 'n', 'R']:
        downRotate(int(a[6]))
    elif a[:4] == ['P', 'E', 'E', 'K']:
        peek()
    elif a[:3] == ['D', 'U', 'P']:
        duplicate()
    elif a[:2] == ['-', '1']:
        break
    else:
        print("다시 입력하세요!!")
        continue