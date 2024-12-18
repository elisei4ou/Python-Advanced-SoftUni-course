def find_smallest_subset(uni, sets):
    count = 0
    used_sets = []

    while uni:
        biggest_set = max(sets, key=lambda x: len(uni.intersection(x)))
        uni -= biggest_set
        used_sets.append(sorted(biggest_set))
        count += 1

    result = f"Sets to take ({count}):\n"
    for s in used_sets:
        result += "{ " + ', '.join([str(x) for x in s]) + " }\n"
    return result


universe = {int(x) for x in input().split(", ")}
i = int(input())
all_sets = []

for n in range(i):
    all_sets.append(set(int(x) for x in input().split(", ")))

print(find_smallest_subset(universe, all_sets))


