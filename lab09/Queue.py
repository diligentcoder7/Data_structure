import sys
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [0] * MAX_QSIZE

    def isEmpty(self) : return self.front == self.rear
    def isFull(self) : return self.front == (self.rear+1)%MAX_QSIZE

    def enqueue(self, item): # 삽입
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item
        else:
            print("overflow", end=' ')
            for k in self.items:
                print(k, end=' ')
            print()
            sys.exit(0)

    def dequeue(self): # 삭제
        if not self.isEmpty():
            self.items[self.front+1] = 0
            self.front = (self.front+1) % MAX_QSIZE # front 포인터가 시계방향으로 한 칸 이동
            return self.items[self.front]
        else:
            print('underflow')
            sys.exit(0)

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[0:]
        else:
            out = self.items[0:self.front+1] + self.items[self.front+1:MAX_QSIZE]
        for j in out:
            print(j, end=' ')
        print()

queue_size = int(input())
MAX_QSIZE = queue_size
n = int(input())
q = CircularQueue()
for i in range(n):
    a = input().split()
    if a[0] == 'I':
        q.enqueue(int(a[1]))
    elif a[0] == 'P':
        q.display()
    elif a[0] == 'D':
        q.dequeue()
    else:
        print("잘못 입력하였습니다. 남은 횟수는 ", n-i-1, "번입니다.")