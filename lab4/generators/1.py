def squares_generator(N):
    for i in range(1, N + 1):
        yield i * i
N = 5
squares = squares_generator(N)

print("Squares of numbers up to", N, ":")
for square in squares:
    print(square)
