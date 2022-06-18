import sys
MAX_QSIZE = 10
class CircularDeque:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QSIZE

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def addRear(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def deleteFront(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]
        else:
            print('underflow')
            sys.exit(0)

    def getFront(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0: self.front = MAX_QSIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear];
            self.rear = self.rear - 1
            if self.rear < 0: self.rear = MAX_QSIZE - 1
            return item
        else:
            print('underflow')
            sys.exit(0)

    def getRear(self):
        return self.items[self.rear]

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]
        else:
            out = self.items[self.front + 1:MAX_QSIZE] \
                  + self.items[0:self.rear + 1]
        print(' ', end='')
        for j in out:
            print(j, end=' ')
        print()

n = int(input())
q = CircularDeque()
for i in range(n):
    a = input()
    if a[:2] == 'AF':
        q.addFront(int(a[3:]))
    elif a[:2] == 'AR':
        q.addRear(int(a[3:]))
    elif a[:2] == 'DF':
        q.deleteFront()
    elif a[:2] == 'DR':
        q.deleteRear()
    elif a[0] == 'P':
        q.display()
    else:
        print("잘못 입력하였습니다. 남은 횟수는 ", n-i-1, "번입니다.")