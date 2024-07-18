def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

# Test
multiplication_table(5)
# Output:
#    1    2    3    4    5 
#    2    4    6    8   10 
#    3    6    9   12   15 
#    4    8   12   16   20 
#    5   10   15   20   25
