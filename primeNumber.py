from math import sqrt,floor
def checkPrimeNumber(num):
    c=0
    if(num>1):
        for i in range(2,floor(sqrt(num)+1)):
            if(num%i==0):
                c+=1
                break
        if(c==0):
            return True
        else:
           return False
    else:
        return False

lower=int(input("Enter your lower limit: "))
upper=int(input("Enter your upper limit: "))
res=[prime_number for prime_number in range(lower,upper+1) if checkPrimeNumber(prime_number)]
print(res)
print(len(res))


