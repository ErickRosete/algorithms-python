def karatsubaString(num1, num2):
    if(num1 < 10 or num2 < 10):
        return num1 * num2
    
    n = len(str(num1))
    nby2 = n // 2
    a = int("0" + str(num1)[:-nby2])
    b = int("0" + str(num1)[-nby2:])
    c = int("0" + str(num2)[:-nby2])
    d = int("0" + str(num2)[-nby2:])

    ac = karatsubaString(a,c)
    bd = karatsubaString(b,d)
    ad_plus_bc = karatsubaString(a + b, c + d) - ac - bd
    ac = int(str(ac) + "0" * (2 * nby2))
    ad_plus_bc = int(str(ad_plus_bc) + "0" * (nby2))
    prod = ac + bd + ad_plus_bc
    return prod

def karatsuba(num1, num2):
    if(num1 < 10 or num2 < 10):
        return num1 * num2
    
    n = numLength(num1)
    nby2 = n // 2
    a = num1 // 10**(nby2)
    b = num1 % 10**(nby2)
    c = num2 // 10**(nby2)
    d = num2 % 10**(nby2)
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
    prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
    return prod

def numLength(num):
    i = 0
    while(num > 0):
        num //= 10
        i += 1
    return i


mult = karatsubaString(3141592653589793238462643383279502884197169399375105820974944592,\
              2718281828459045235360287471352662497757247093699959574966967627)
print(mult)

