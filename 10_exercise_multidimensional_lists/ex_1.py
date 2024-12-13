rows = input().split("|")

matrix = [[col for col in row.split()]for row in rows]

[print(*x, end=" ") for x in matrix[::-1] if x]