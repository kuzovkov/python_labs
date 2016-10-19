from math import sqrt

formula = 'f(x)=0.7*x2-sqrt(3)*x +4.8' 
a = 0
b = 2
eps = 0.0001

def function( x ):
    return 0.7 * x * x - sqrt( 3 ) * x + 4.8
