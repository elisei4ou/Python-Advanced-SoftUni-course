numbers = [float(x) for x in input().split()]
unique_n = set()

for z in numbers:
    if z not in unique_n:
        print(f"{z} - {numbers.count(z)} times")
    unique_n.add(z)
