"""
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)
"""

"""
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
"""
"""
# Que pueden hacer las tuplas?
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
"""
"""
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
"""
my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # salida: [2, 4, 6]
print(type(my_list)) # salida: <class 'list'>
tup = tuple(my_list)
print(tup) # salida: (2, 4, 6)
print(type(tup)) # salida: <class 'tuple'>