def greedy_approach(coins, the_sum):
    idx = 0
    collected_coins = {}
    coins = sorted(coins, reverse=True)

    while the_sum > 0 and idx < len(coins):

        count_of_coins = the_sum // coins[idx]
        the_sum = the_sum % coins[idx]

        if count_of_coins:
            collected_coins[coins[idx]] = count_of_coins

        idx += 1

    if the_sum > 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(collected_coins.values())}\n"

        for coin, value in collected_coins.items():
            result += f"{value} coin(s) with value {coin}\n"

        return result


possible_coins = [int(x) for x in input().split(", ")]
desired_sum = int(input())

print(greedy_approach(possible_coins, desired_sum))