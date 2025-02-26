'''
#list 
L=[]
print(L)
L=list()
print(L)

#list of numbers
L=[9,1,2,9,3,5,9,20,2]
print(L[2])
print(L[2:7])

L=[9,1,2,9,3,5,9,20,2]
print(L.count(1))#1
print(L.count(9))#3

#add ele
L.append(30)#30 will be added at the end
print(L)
L.extend([6,1,9])#multi ele added at the end
print(L)
L.insert(2,100)#at index 2 ele 100 will be added
print(L)

#remove ele
x=L.pop(4)#remove ele at index 4
print(L)
print(x)

L.remove(2)#remove ele with value 2
print(L)

L.clear()
print(L)

L=[9,1,2,9,3,5,9,20,2]
L.reverse()
print(L)

L.sort()
print(L)
L.sort(reverse=True)
print(L)
'''
D={4:15,14:50,9:19,14:20}

print(D[4])#15
print(D.get(4))#15
print(D)

