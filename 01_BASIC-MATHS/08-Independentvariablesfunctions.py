#HelloWOrld,9.1
#date: 18-july-2026 saturday.

#this program is about : 
#we can also have function with independept variable such as : 
#f(x,y)= 2*x + 3*y 

#Since we have indepedent vatiable (the output(f(x,y)=2*x+3*y ) we need to plot the graph on three dimensions to produce the plane of values. 

#here is the program. 


from sympy import * 
from sympy.plotting import plot3d
x,y = symbols('x,y') 
f = 2*x+ 3*y 
plot3d(f) 