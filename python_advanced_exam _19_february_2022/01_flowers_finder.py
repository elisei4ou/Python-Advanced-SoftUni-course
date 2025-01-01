from collections import deque

vowels = deque(char for char in input().split())
consonants = [char for char in input().split()]

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
flower_found = False

while vowels and consonants:

    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower, letters in flowers.items():
        flowers[flower] = flowers[flower].replace(vowel, "")
        flowers[flower] = flowers[flower].replace(consonant, "")

        if not flowers[flower]:
            print(f"Word found: {flower}")
            flower_found = True
            break

    if flower_found:
        break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")