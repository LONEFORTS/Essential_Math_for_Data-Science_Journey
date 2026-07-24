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