from collections import deque

line_with_kids = deque(input().split())
rotates = int(input()) - 1

while len(line_with_kids) > 1:
    line_with_kids.rotate(-rotates)
    left_buddy = line_with_kids.popleft()
    print(f"Removed {left_buddy}")

print(f"Last is {line_with_kids[0]}")