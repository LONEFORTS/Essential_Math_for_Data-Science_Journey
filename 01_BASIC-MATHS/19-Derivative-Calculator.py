#HElloworld 11.56am 
#date.24JULY2026 

#About Derivatives : 

#A derivative tells us the slope of a given function, and it is useful in machine learning and other mathematical algorithms.
#ANd useful with gradient descent  

def derivative_x(f,x,step_size): 
    m= (f(x+step_size) - f(x) / ( ( x+ step_size)-x) 
    return m 

def my_function(x): 
    return x**2 

step_at_2 = derivative_x(my_function,2,.00001)
print(step_at_2) 


""" 
Now here is the Explanation which I wrote in notes today... 

The purpose of this program is to estimate the dervivative slope of a functiona. 

- a derivative tells us how quickly a function changes with respect to x.  

1.In The first line of def derivative_x(f,x,step_size): 
-It defines a python function named derivatice_x. The keyword 'def' is used to declare or create the function named derivative_x and it has parameters. 

- here is meaning of parameters: 
parameter f : Represents the mathematical function whose derivative we want to calculate. Instead of a passing a number we entirely passed the whole function 😅 as (my_function) 

- The parameter x : it is the point where we want to find the derivative.
- for example : if x=2, the programs find the slop at x=2, Now here is the last parameter which is :
- the parameter named step_size : 
it is a very small number that tells the program how far move from the 'x'. 
- In this program, step_size is 0.00001, so when the x=2 the step_sizz becomes 2.00001 and the IMPORTANTLY :
- the smaller the step_size is the accurate the approximation usually becomes, however it is too small such as 0.000000000001 it can lead to errors in computers floating point arithmetic. 
- AND if it is too large such as 2 or 1... the approximation becomes poor be ausse the two points are not close enough, 
in practice value like 0.00001, 0.001, and 0.0001 are commonly used. 


2. now about the second line, 
m = f(x+step_size)-f(x)/((x+step_size)-x) 

it calculates the approximate derivative using that formula. 

1.Here ncis the variable that stores the calculated slop. the expression f(x+step_size) Evaluates the function at orginal point slightly to the right x, while f(x) evaluates the function at the orginal point.
-Subtracting these two values tells us how much the function output has changed after moving a small distance.
- The Denominator ((x+step_size)-x)  calculates how much input value has changed, in this program the input changes by .00001, which is the value of step size. 

"""