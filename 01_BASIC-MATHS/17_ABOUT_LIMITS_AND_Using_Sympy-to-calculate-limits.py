#HelloWOrld.9.32.pm
#date.23-july-2026.thursday. 


#This program is about the limits in maths and python.

#About limits : for example : if we take this function f(x) = 1/x to graph it will get closer to zero or approach to zero but never reach it. 
#THe way we express this is through a limit which i just wrote in my notebook. 


from sympy import * 
x = symbols('x')
f = 1/x 
result = limit(f,x,oo)  
print(result) 