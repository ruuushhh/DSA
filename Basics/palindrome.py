def reverse_a_number(n):
    reverse = 0
    while n!=0:
        reverse = reverse*10 + n%10
        n = n//10
    return reverse

n = int(input())
reverse = reverse_a_number(n)
if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")