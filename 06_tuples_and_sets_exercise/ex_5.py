n = int(input())
the_longest = []

for _ in range(n):
    first_range, second_range = input().split("-")
    f_s, f_e = first_range.split(",")
    f_s = int(f_s)
    f_e = int(f_e)

    s_s, s_e = second_range.split(",")
    s_s = int(s_s)
    s_e = int(s_e)

    first_set = set([x for x in range(f_s, f_e + 1)])
    second_set = set([x for x in range(s_s, s_e + 1)])
    intersection = first_set.intersection(second_set)

    if len(intersection) > len(the_longest):
        the_longest = intersection

print(f"Longest intersection is [{', '.join([str(x) for x in the_longest])}] with length {len(the_longest)}")


