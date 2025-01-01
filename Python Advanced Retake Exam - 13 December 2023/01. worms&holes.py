from collections import deque

worms = [int(worm) for worm in input().split()]
holes = deque(int(worm) for worm in input().split())

matches = 0
worms_at_the_start = len(worms)

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_hole != current_worm:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

    else:
        matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if matches == worms_at_the_start:
    print("Every worm found a suitable hole!")

elif not worms:
    print("Worms left: none")

else:
    print(f"Worms left: {', '.join([str(w) for w in worms])}")

if not holes:
    print("Holes left: none")

else:
    print(f"Holes left: {', '.join([str(h) for h in holes])}")