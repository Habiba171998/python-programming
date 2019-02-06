def power(num1,num2):
    if(num2==1):
        return(num1)
    if(num2!=1):
        return(num1*num2(num1,num2-1))
num1=int(input())
num2=int(input())
print(power(num1,num2))
