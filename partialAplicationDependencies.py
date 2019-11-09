# PARTIAL APLICATION WORKING WITH DEPENDENCIES
__author__ = "Gabriel Avendaño, Valentina Bernal, Daniela Duque"

result = lambda res : print(f'Your answer is {res}')

##################### Example 1
print ('Example 1')

add = lambda x, y : x + y
mul = lambda x : lambda y : y*x
mul3 = mul(3)


def add_mul (x,y):
    res = add(x, y)
    res = mul3(res)
    result (res)

add_mul(2,3)

##################### Example 2
print ('Example 2')

module = lambda x : lambda y : y % x
lastdigit = module(10)

def apply_function (x,f):
    res = f(x)
    result (res)

last_dig = lambda x : apply_function (x, lastdigit)

last_dig(3930908)


##################### Example 3
print ('Example 3')

def gcd_private (a, b):
    if b == 0:
        return a
    else :
        return gcd_private(b,module (b)(a)) 

def max_with_function  (a , b , f):
    if a >= b : 
        return f(a,b)
    else:
        return f(b,a)

gcd = lambda a, b :  max_with_function(a, b, gcd_private) 

printGcd = lambda a, b :  result(gcd(a,b))

printGcd(14, 52)




