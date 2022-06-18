class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top=[]

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
                    return False
    return stack.isEmpty()

# str=("{ A[(i+1)] = 0; }", "if( (i==0) && (j==0)", "A[ (i+1) ) = 0;")
number_of_try = int(input("연산 횟수를 입력하세요 : "))
for i in range(number_of_try):
    s = input("문장을 입력하세요 : ")
    number_of_Brackets = 0
    for j in s:
        if j in ('{', '[', '(', '}', ']', ')'):
            number_of_Brackets += 1
        else:
            continue
    m = checkBrackets(s)
    if m == False:
        print("Wrong_", number_of_Brackets, sep='')
    else:
        print("OK_", number_of_Brackets, sep='')