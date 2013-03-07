from sympy import solve

res = solve('Eq(F, m*a)', 'a')
print res


res = solve('Eq(X, 1/2*a*t**2)', 't')
print res

res = solve('Eq(U, X*R)', 'R')
print res

# Sympy treats e, i and other important characters differently. We need to do
# something about it.
