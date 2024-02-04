def reverse_a_number(n):
    reverse = 0
    while n!=0:
        reverse = reverse*10 + n%10
        n = n//10
    return reverse

n = int(input())
print(reverse_a_number(n))