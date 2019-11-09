# PARTIAL APLICATION WORKING WITH LIST
__author__ = "Gabriel Avendaño, Valentina Bernal, Daniela Duque"

myList = [1, 2, 3, 4, 5, 6]
print ('myList : ', myList)

# with map

square = lambda x : x ** 2
print ('myList squared : ', list(map(square, myList)))

# with reduce

from functools import reduce

add = lambda x, y: x + y
print ('sum all elements of myList : ' , reduce (add , myList))


# with filter 

isEven = lambda x :  x % 2 == 0
print ('list of even numbers in myList : ', list(filter(isEven, myList)))


