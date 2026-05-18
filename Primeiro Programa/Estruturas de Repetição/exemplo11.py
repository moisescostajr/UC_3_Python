import random
n = [ 2, 4, 7, 1, 5, 3, 6, 8, 9, 10]
random.shuffle(n)
n.sort()
print(n)
n.reverse()
print(n)

copia = list(n)
print(copia)

n.clear()
print(n)
print(copia)
