import wcom

def FP(p,i,n): #GG
    f = p*(1+(i/100))**n
    return f

def PF(f,i,n): #GG
    p = f/((i/100)+1)**n
    return p

def FA(a,i,n): #GG
    i =i/100
    f = a*((1+i)**n - 1)/i
    return f

def AF(f,i,n): #GG
    i=i/100
    a = (f*i) / ((1+i)**n - 1)
    return a

def AP(p,i,n): #GG
    i=i/100
    a= (p*i*(1+i)**n)/(((1+i)**n) - 1)
    return a

def PA(a,i,n): #GG
    i=i/100
    p = a*((((1+i)**n) -1)/(i*((1+i)**n)))
    return p

def AG(g,i,n):
    i=i/100
    a = g * ((i+1)**n -(i*n) -1)/(i*(i+1)**n - 1)
    return a

def PG(g,i,n):
    i=i/100
    p = g*(((i+1)**n - i*n - 1)/(i**2 * (1+i)**n))
    return p

def AEq(a0,g,i,n):
    if g > 0:
        aeq = a0 + AG(g,i,n)
    else:
        aeq = a0 - AG(g,i,n)
    return aeq

def PEq(a,g,i,n):
    if g > 0:
        peq = PA(a,i,n) + PG(g,i,n)
    else:
        peq = PA(a,i,n) - PG(g,i,n)
    return peq

print(FA(500,8,3))
