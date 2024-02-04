def pattern(num: int):
    for _ in range(0, num):
        for _ in range(0, num):
            print("*", end= " ")
        print()

num = int(input())
pattern(num)