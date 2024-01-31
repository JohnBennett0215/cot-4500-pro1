"""
Test for bisection method
"""

def f(x):
    return pow(x, 3) + 4 * pow(x, 2) - 10
    
tol = 0.0001
left = -4
right = 7

max = 1000
i = 0

while(abs(right - left) > tol and i < max):
    i = i + 1
    p = (left + right) / 2
    
    if (f(left) < 0 and f(p) > 0):
        right = p
    else:
        left = p
        
print(i,"\n")

"""
Test for Fixed Point Iteration
"""

pn = 1
tol = 0.000001
n = 1000


i = 1
while (i <= n):
   p = g(p)
   if (abs(p - pn) < tol):
        print(p, "Success")
        break
        
   i = i + 1
   pn = p
   
"""
Test for Newton Raphson method
"""
p = -4
pn = 0.0001
tol = 0.0001
maxi = 1000
i = 1

while ( i <= maxi):

    if(fp(p) != 0):
    
        pn = p - f(p) / fp(p)
        
        if (abs(pn - p) < tol):
        
            print(i, "\n")
            
            print("Success\n")
            
            break
            
        i = i + 1
        
        p = pn
        
    else:
    
        print("Unsuccessful")
  
"""
Test for Approximation Method
"""
error_tolerance = 0.000001

guess = 1.0
i = 0

while True:
    next_guess = 0.5 * (guess + 5 / guess)
    
    print(f"iteration {i + 1}: {next_guess}")
    
    if abs(next_guess - guess) < error_tolerance:
        break
        
    guess = next_guess
    i += 1
    
print(f"\nApproximated square root of 5: {next_guess}\n")
print(f"Number of iterations: {i + 1}\n")
