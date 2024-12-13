n = int(input())
all_guest = set()

for _ in range(n):
    guest = input()
    all_guest.add(guest)

the_came_guests = input()
while the_came_guests != "END":
    if the_came_guests in all_guest:
        all_guest.remove(the_came_guests)
    the_came_guests = input()

print(len(all_guest))
[print(g) for g in sorted(all_guest)]