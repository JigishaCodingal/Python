'''
for i in range(15):
    print(i)

#range(5): 0 to 14
print("--------------------")
for i in range(10,15):#10 to 14
    print(i)
print("--------------------")
for i in range(10,20,4):#10, 14, 18
    print(i)
print("--------------------")
for i in range(20,10,-4):#20  16  12  
    print(i)
print("--------------------")
for i in range(20,15,-1):#20 19 18 17 16  
    print(i)

# Display summation of n natural numbers : 1, 2, 3, 4.......n

sum=0# 0+ 1 +2 +3 ......n
n=int(input("Enter n: "))
for i in range(1,n+1):
    sum=sum+i
print("Summation of ",n,"natural numbers = ",sum)
'''

#reverse a string

s1=input("Enter a String")#abc
s2=""
for x in s1: # x : a , b, c
    s2=x+s2 #s2= a + ""= "a" => s2= "b'+ 'a'='ba' => s2= 'c'+'ba'='cba'
print("Original String",s1)
print("New String",s2)

