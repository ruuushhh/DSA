def pattern(num: int):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

num = int(input())
pattern(num)