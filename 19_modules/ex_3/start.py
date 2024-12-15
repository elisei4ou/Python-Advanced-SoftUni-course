def print_triangle(n):
    def upper_part(n):
        for row in range(1, n + 1):
            for col in range(1, row+1):
                print(col, end=" ")
            print()

    def lower_part(n):
        for row in range(n, 1, -1):
            for col in range(1, row):
                print(col, end=" ")
            print()

    upper_part(n)
    lower_part(n)