from collections import deque

ramens = [int(el) for el in input().split(", ")]
people = deque(int(el) for el in input().split(", "))

while ramens and people:
    ramen = ramens.pop()
    person = people.popleft()

    if ramen == person:
        continue
    elif ramen > person:
        ramen -= person
        ramens.append(ramen)
    elif ramen < person:
        person -= ramen
        people.appendleft(person)

if not people:
    print(f"Great job! You served all the customers.")
    if ramens:
        print(f"Bowls of ramen left: {', '.join([str(r) for r in ramens])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(p) for p in people])}")


