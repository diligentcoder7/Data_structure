from dlist import DList
if __name__ == '__main__':
    s = DList()
    number_of_try = int(input("연산의 개수를 입력하세요 : "))

    for i in range(number_of_try):
        a = list(input().split())
        if a[0] == 'A':
            s.add(int(a[1]), a[2])
        elif a[0] == 'D':
            s.delete(int(a[1]))
        elif a[0] == 'G':
            s.get(int(a[1]))
        elif a[0] == 'P':
            s.print()
        else:
            print("값을 잘못 입력하셨습니다. 함수를 종료합니다.")
            break