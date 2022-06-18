from Tree import binarytree
if __name__ == '__main__':
    t = binarytree()
    n1 = t.Node(20)
    n2 = t.Node(30)
    n3 = t.Node(50)
    n4 = t.Node(70)
    n5 = t.Node(90)
    n6 = t.Node(120)
    n7 = t.Node(130)
    n8 = t.Node(80)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    n6.left = n7
    n6.right = n8
    t.root = n1

    t = binarytree()
    num = int(input())
    list = [n1, n2, n3, n4, n5, n6, n7, n8]
    if num > 8:
        print(-1)
    else:
        a = list[num-1]
        t.PRINT(a)
