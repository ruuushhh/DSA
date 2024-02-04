
#Brute Force
# def gcd(num1: int, num2: int):
#     gcd = 1
#     for i in range(1, max(num1,num2)):
#         if num1%i == 0 and num2%i == 0:
#             gcd = max(gcd, i)
#     return gcd

# num1 = int(input())
# num2 = int(input())

# print(gcd(num1, num2))

#Recursion
def gcd(num1, num2):
    if num2 == 0:
        return num1
    
    return gcd(num1, num2%num2)

num1 = int(input())
num2 = int(input())

print(gcd(num1, num2))
