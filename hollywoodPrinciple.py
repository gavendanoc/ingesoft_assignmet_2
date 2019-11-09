#  Hollywood principle
__author__ = "Gabriel Avendaño, Valentina Bernal, Daniela Duque"

##################### Example 1
print ('Example 1\n')

def divide (top, bottom, ifZero, ifOk):
    if bottom == 0:
        ifZero()
    else:
        ifOk(top / bottom)


ifZero = lambda : print ('bad')
ifOk = lambda res :  print (f"good {res}")


divide1 = lambda top, bottom : divide (top, bottom, ifZero, ifOk )  

divide1(5, 0)
divide1(100, 5) 

##################### Example 2

print ('\nExample 2\n')

def exp (base, expo, ifZeroexpzero, ifOk):
    if base == 0 and expo ==0:
        ifZeroexpzero()
    else:
        ifOk(base** expo)


ifZeroexpzero = lambda : print ('Impossible')
ifOk = lambda res :  print (f"Your answer is {res}")


exp1 = lambda base, expo : exp (base, expo, ifZeroexpzero, ifOk )  
exp1(0, 0)
exp1(3, 4) 
















