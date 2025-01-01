from collections import deque

portions = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))

mountains = deque([80, 90, 100, 60, 70])
mountains_names = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])
conquered_peaks = []

while portions and stamina:

    if mountains:
        current_portion = portions.pop()
        current_stamina = stamina.popleft()
        current_mountain = mountains.popleft()

    else:
        break

    sum = current_stamina + current_portion

    if sum >= current_mountain:
        conquered_peaks.append(mountains_names.popleft())
        continue

    else:
        mountains.appendleft(current_mountain)

if not mountains:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

elif mountains:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
for conquered_peak in conquered_peaks:
    print(conquered_peak)
