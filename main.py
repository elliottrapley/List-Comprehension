'''
List Comprehension
'''

squares = [] 

for x in range(10):
  squares.append(x ** 2)
print(squares)


# This is the same as writing the code above
print([x**2 for x in range(10)]) 

# The output will be the same

'''
Conditionals in List Comprehension
'''

combs = []

for x in [1, 2, 3]:
  for y in [3, 1, 4]:
    if x != y:
      combs.append((x, y))

print(combs)
print("The same output")
print([(x,y)for x in[1,2,3] for y in [3,1,4] if x != y])


