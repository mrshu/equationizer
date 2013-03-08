from sympy import solve, Symbol, sympify

res = solve('Eq(F, m*a)', 'a')
print res


res = solve(sympify('Eq(X, 1/2*a*t**2)', locals={'E': Symbol('E')}), 't')
print res

res = solve(sympify('Eq(U, I*R)', locals={'I': Symbol('I')}), 'R')
print res

# Sympy treats e, i and other important characters differently. We need to do
# something about it.
