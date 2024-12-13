from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence = int(input())
left_bullets = gun_barrel_size
bullets_price = 0

while bullets and locks:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()
    bullets_price += price_per_bullet

    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    elif current_bullet <= current_lock:
        print("Bang!")
    left_bullets -= 1

    if left_bullets == 0:
        if bullets:
            print("Reloading!")
        if len(bullets) > gun_barrel_size:
            left_bullets = gun_barrel_size
        else:
            left_bullets = len(bullets)

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_price}" )

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")