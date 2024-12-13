n = int(input())
unique_el = set()

for _ in range(n):
    some_elements = input().split()

    for e in some_elements:
        unique_el.add(e)

[print(v) for v in unique_el]