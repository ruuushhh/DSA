def pattern(num: int):
    for i in range(1, num+1):
        for _ in range(0, i):
            print('*', end=" ")
        print()

num = int(input())
pattern(num)