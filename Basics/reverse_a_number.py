def reverse_a_number(n):
    x = str(n)
    return int(x[::-1])

n = int(input())
print(reverse_a_number(n))