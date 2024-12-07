n, m = [int(x) for x in input().split()]
first_set = set()
second_set = set()

for _ in range(n):
    number = input()
    first_set.add(number)

for _ in range(m):
    number = input()
    second_set.add(number)

same_elements = first_set.intersection(second_set)
[print(z) for z in same_elements]