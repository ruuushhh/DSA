def armstrong(x:int):
    original = x
    count = 0
    temp = x
    while temp != 0:
        count +=1
        temp //=10
    sumpow = 0
    while x!=0:
        digit = x%10
        sumpow += pow(digit, count)
        x//=10
    return sumpow == original

num = int(input())

if armstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")


