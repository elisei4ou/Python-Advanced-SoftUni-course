some_input = list(input())
all_el = set()

for every_el in sorted(some_input):
    if every_el not in all_el:
        print(f"{every_el}: {some_input.count(every_el)} time/s")
    all_el.add(every_el)
