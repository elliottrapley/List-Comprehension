'''
List Comprehension
'''

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)  # output => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# with list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)  # output => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


'''
Conditionals in List Comprehension
'''

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(combs)

# with list comprehension
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

'''
Nested List Comprehensions
'''

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
res = [[row[i] for row in matrix] for i in range(4)]

print(res)

# =========================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = []
for i in range(4):
    res.append([row[i] for row in matrix])

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(res)

# =========================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = []
for i in range(4):
    res_row = []
    for row in matrix:
        res_row.append(row[i])
    res.append(res_row)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(res)

# =========================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = list(zip(*matrix))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(res)