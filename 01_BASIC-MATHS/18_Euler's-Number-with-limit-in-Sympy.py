#HelloWorld 9.37PM 
#DATE-23-JULY-2026.THURSDAY. 



#Well...When we calculate Euler's number with limits Sympy immediately recognizes it as Euler's number. but we can also use the evalf() to print the actual numbers. 

#here's the example of it: 

from sympy import * 

n = symbols('n') 
f = (1+n/n)**n 
result = limit(f,n,oo) 
print(result) 
print(result.evalf())		