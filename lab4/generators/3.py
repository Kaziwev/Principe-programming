def squares_generator(N):
    for i in range(0, N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
    
N = int(input())
squares = squares_generator(N)
for square in squares:
    print(square)