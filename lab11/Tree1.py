class binarytree:
    class Node:
        def __init__(self, item, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def PRINT(self, n):
        if n != None:
            print(n.item, end=' ')
            if n.left:
                print(n.left.item, end=' ')
                if n.right:
                    print(n.right.item, end=' ')
            elif n.right:
                print(n.right.item, end=' ')
        else:
            print(-1)

    n1 = Node(20)
    n2 = Node(30)
    n3 = Node(50)
    n4 = Node(70)
    n5 = Node(90)
    n6 = Node(120)
    n7 = Node(130)
    n8 = Node(80)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    n6.left = n7
    n6.right = n8