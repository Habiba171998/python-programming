def power(base,ex):
    if(ex==1):
        return(base)
    if(ex!=1):
        return(base*power(base,ex-1))
base=int(input())
ex=int(input())
print(power(base,ex))
