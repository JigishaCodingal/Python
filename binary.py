B=int(input("Enter big number : "))
S=int(input("Enter small number : "))

while(S):
    n=S
    S=B%S
    B=n
HCF=B
print("HCF =",B)
print("LCM=",B*S/HCF)
#hcf*lcm=a*b
#3*lcm=24*9
#lcm=24*9/3
