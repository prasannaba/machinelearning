# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:57:31 2019

Description:
    Newton Raphson method

    y = f(x)
    find tangent, slope i.e derivative at point (x0, y0), f'(x0)
    
    f'(x0) = (y - y0)/(x - x0) 

    (y - y0) = f'(x0) (x - x0) is tangent line. This will intercept x-axis. 

    y0 = f(x0), rearranging for x

    x = x0 + (y - f(x0))/f'(x0)

    if y = 0, we get x-intercept of tangent that is (x1, 0)

    x1 = x0 - f(x0))/f'(x0)

    In practice, we stop when abs(f(x1), f(x0))<=some threshold like 0.01, the value of x at this happens is the root.
    We say the process has converged to a solution i.e we have found the root.
    
    As '(x) tends to zero then f(x) is not changing much. That is the root.

@author:Prasanna
"""
# %%
epsilon = 0.01
# %%
y = 27
guess = y/2.0
numGuesses = 0
while(abs(guess**3 - y) >= epsilon):
    numGuesses += 1
    guess = guess - ((guess**3 - y)/(3*guess**2))
print('numGuesses = ' + str(numGuesses))
print('Cube root of ' + str(y) + ' is about ' + str(guess))
# %%
# find the root of equation f(x)=0
# f(x)= x**2-4=0, x**2=4
x = 100
numGuesses=0
while(abs(x**2-4) >= 0.01):
    numGuesses += 1
    print(f'Value of x: {x}')
    print(f'Function: {(x**2-4):0.4f}')
    print(f'Derivative: {(2*x):0.4f}')
    x = x - ((x**2-4)/(2*x))
print('numGuesses = ' + str(numGuesses))
print('Root of  x is about ' + str(x))
# %%
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(-4, 4, 20)
y = x**3-27
plt.plot(x, y)
# %%
# find the root of equation x**2+x-3=0
# x**2+x=3
x = 0.1
numGuesses=0
while(abs(x**2+x-3) >= epsilon):
    numGuesses += 1
    print(f'Value of x: {x}')
    print(f'{(x**2+x-3):0.3} function')
    print(f'{(2*x+1):0.4f} derivative')
    x = x - ((x**2+x-3)/(2*x+1))
print('numGuesses = ' + str(numGuesses))
print('Root of  x is about ' + str(x))
# %%
import scipy.optimize as optimize
# %%
# root of an equation
def func(x):
    return(x**2+x-25)
optimize.newton(func, 0.1)
# %%
import numpy as np
# %%
# x**2+x+25
coeff = [1, 1, 25]
np.roots(coeff)
# %%
# x**2+x-25
coeff = [1, 1, -25]
np.roots(coeff)
# %%
# x+27
coeff = [1, 27]
np.roots(coeff)
# %%