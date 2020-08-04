# Program to calculate compound_interest

def compound_interest(p,r,t):
    CI=p*(1+(r/100))**t
    return CI
print(compound_interest(int(input()),float(input()),float(input())))    