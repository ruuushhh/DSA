def is_prime(num: int):
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return "Not Prime"
        
    return "Prime"

num = int(input())
print(is_prime(num))