first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command, command1, *data = input().split()

    if command + " " + command1 == "Add First":
        for z in data:
                first_set.add(int(z))

    elif command + " " + command1 == "Add Second":
        for z in data:
                second_set.add(int(z))

    elif command + " " + command1 == "Remove First":
        for z in data:
            first_set.discard(int(z))

    elif command + " " + command1 == "Remove Second":
        for z in data:
            second_set.discard(int(z))

    elif command + " " + command1 == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

sorted_first_set = sorted(first_set)
sorted_second_set = sorted(second_set)

print(*sorted_first_set, sep=", ")
print(*sorted_second_set, sep=", ")


