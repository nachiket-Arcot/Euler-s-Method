
function = lambda x,y: x + (1/2)*(y**2) #Replace expression with your function

def euler(x0, y0, x_f, h):

    """
    Approximates the y value of a function given an initial condition using Euler's Method.
    Parameters: 

    x0: x value of the initial condition
    y0: y value of the initial condition
    x_f: Target x value that you want to approximate the y value of
    h: Step Size 
    """
    y_n = y0
    x_n = x0
    rep = 0 #Number of iterations
    
    #Looping until x_n reaches x_f to approximate y value of function 
    while x_n < x_f:
        y_n = y_n + h * (function( x_n , y_n )) 
        x_n = x_n + h
        rep +=1
        print(f"{rep}: x = {x_n}, y = {y_n}")


euler(-2, 0, 2, 0.0001)
