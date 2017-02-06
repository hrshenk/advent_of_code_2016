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
        
print 1*2*3