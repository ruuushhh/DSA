def count_digits(x: int):
  count = 0
  while (x!=0):
    x=x//10
    count+=1
  return count


n = int(input())
print(count_digits(n))