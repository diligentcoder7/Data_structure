class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def add(self, r, e):
        p = self.head
        for i in range(r):
            p = p.next
        t = p.prev
        n = self.Node(e, t, p)
        t.next = n
        p.prev = n
        self.size += 1

    def delete(self, r):
        if self.size < r:
            return
        p = self.head
        for i in range(r):
            p = p.next
        t = p.prev
        f = p.next
        t.next = f
        f.prev = t
        self.size -= 1

    def get(self, r):
        p = self.head
        for k in range(r):
            if p.next != None:
                p = p.next
            else:
                break
        if p.item == None:
            print("invalid position")
        else:
            print(p.item)


    def print(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, end='')
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass
