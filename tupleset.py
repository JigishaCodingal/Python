
#tuple
#empty tuple

T=()
print(T)
T=tuple()
print(T)


#single ele
T=(30,)
print(T,type(T))
T=(30)#not a tuple but it is a number
print(T,type(T))


#Tuple with many ele
T=(6,1,8,1,2,9,10)#immutable
L=[6,1,8,1,2,9,10]#mutable
L[2]=100
print(L)
T[2]=100

T=(6,1,8,1,2,9,10)
print(sum(T))
print(max(T))
print(min(T))

s1={6,9,1,6,2,0,2}
s1.add(40)
print('s1 : ',s1)
s2={2,4,0}
print('s2 : ',s2)
print(s1.difference(s2))#s1-s2 , common ele are removed from s1
print(s1.symmetric_difference(s2))#combine ele of s1 and s2 and then remove common ele
print(s1.union(s2))#all ele will be taken from both the sets
print(s1.intersection(s2))#only common elements

'''
t=(5,7,4)
a,b,c=t
print(b)
t=1,a,2,0,2,c
print(t)

L=list(T)
L=[]
for x in T:
    L.append(x)
'''
