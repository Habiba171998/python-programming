def power(base,exp):
    if(exp==1):
        return(base)
    elif(exp!=1):
        return(base*expo(base,exp-1))
base=input(int)
exp=input(int)
print(power(base,exp))
