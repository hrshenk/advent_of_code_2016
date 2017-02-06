#this is a chinese remainder theorem problem
#in order for the ith disk to be in zero after
#i seconds we must have t = m - (p_i + i) mod m for
#where p_i is the initial postion of the ith disk

def extended_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_euclid(b, a%b)
    return (y, x - y*(a//b), d)


def inv_mod(a, m):
    (x, y, d) = extended_euclid(a, m)
    if d != 1:
        return 0
    else:
        return x%m

def solve_CRT(constraints, moduli):
    product = reduce(lambda x, y: x*y, moduli, 1)
    x = 0
    for a, m in zip(constraints, moduli):
        x += a*inv_mod((product/m), m)*(product/m)
    return x % product
    

#define inputs
#initial postions
initial = [11, 0, 11, 0, 2, 17, 0]
contraints = []
#position counts
moduli = [13, 5, 17, 3, 7, 19, 11]

for i, (p, m) in enumerate( zip(initial, moduli) ):
    contraints.append( ( m - (p + i + 1) ) % m )
for a, m in zip(contraints, moduli):
    print "x = ", a, " mod ", m
    
print solve_CRT(contraints, moduli)