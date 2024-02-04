def pattern(num: int):
    for i in range(1, num+1):
        for _ in range(num+1, i, -1):
            print('*', end=" ")
        print()

num = int(input())
pattern(num)