n = int(input())

sum = 0

for row in range(n):
    list_with_nums = [int(x) for x in input().split()]
    sum += list_with_nums[row]

print(sum)