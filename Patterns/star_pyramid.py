def pattern(num: int):
    k=num-1
    for i in range(0, num):

        for _ in range(0, k):
            print(end=" ")

        k = k-1

        for _ in range(0, i+1):
            print('* ', end="")

        print()

num = int(input())
pattern(num)