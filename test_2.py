def F(n):
    if n < 8:
        F(2 * n)
        print(n)
        F(n + 3)


F(1)
