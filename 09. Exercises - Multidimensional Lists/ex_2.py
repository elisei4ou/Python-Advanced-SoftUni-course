n = int(input())

matrix = [[int(z) for z in input().split()] for x in range(n)]
primary_diagonal = [matrix[el][el] for el in range(n)]
secondary_diagonal = [matrix[el][n - el - 1] for el in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))