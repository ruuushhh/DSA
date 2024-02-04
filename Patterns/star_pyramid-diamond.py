def pattern(num: int):
    k=num-1
    for i in range(0, num):
    
        for _ in range(0, k):
            print(end=" ")

        k = k-1

        for _ in range(0, i+1):
            print('* ', end="")
        print()
    k=num-1
    for i in range(0, num):
        
        for _ in range(0, i):
            print(end=" ")

        for _ in range(0, k+1):
            print('* ', end="")        

        k = k-1

        print()

num = int(input())
pattern(num)