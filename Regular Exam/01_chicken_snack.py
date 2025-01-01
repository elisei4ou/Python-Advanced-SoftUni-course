from collections import deque

money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())
bought_food = 0

while money and prices:
    current_money = money[-1]
    current_price = prices[0]

    if current_money == current_price:
        bought_food += 1
        money.pop()
        prices.popleft()

    elif current_money > current_price:
        bought_food += 1
        money.pop()
        money[-1] += (current_money - current_price)
        prices.popleft()

    elif current_money < current_price:
        money.pop()
        prices.popleft()

if bought_food >= 4:
    print(f"Gluttony of the day! Henry ate {bought_food} foods.")
elif bought_food == 1:
    print(f"Henry ate: {bought_food} food.")
elif 1 < bought_food < 4:
    print(f"Henry ate: {bought_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")

