p =int( input("Enter the pricipal loan amount " ))#is the principal loan amount.
r = int(input("Enter the monthly interest rate " ))/12/100#is the monthly interest rate (annual interest rate divided by 12 months).
n= int(input ("Enter the total of months " ))# is the total number of months.

def interés_mensual(a):
    return  int(p*(r*(1+r)**a) / ((1+r)**a - 1))



for f in range (1,n+1):
    print (interés_mensual(f))