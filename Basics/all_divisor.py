def all_divisor(num: int):
    for i in range(1, int(num**0.5)+1):
        if num%i==0:
            print(i)
            if i != num/i:
                print(int(num/i))

all_divisor(int(input()))