'''
file handling: 

1) open the file
2) modes of operation :
    a) read:
            ->r
            ->file must be existing otherwise it will give us an error
            ->default mode

    b) write
            ->w
            ->if the file is not existing then new file will be created automatically
            ->if the file is already existing then the earlier content of file will be overwritten with new content
            
    c) append
            ->a
            ->if the file is not existing then new file will be created automatically
            ->if the file is already existing then the new content will be added at the end of earlier content

     '''       
      

#1) Read the full file 
fo=open("f1.txt")#read mode
print(fo.read())#reading complete file
fo.close()

#2) read first five characters only

fo=open("f1.txt")#read mode
print(fo.read(5))
fo.close()


#3) count vowels in the file

fo=open("f1.txt")
ch=fo.read(1)
c=0
while ch:#if ch is existing
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        c+=1
    ch=fo.read(1)
print("Total number of vowels : ",c)




#4) count number of lines
fo=open("f1.txt")
ch=fo.read(1)
c=1
while ch:#if ch is existing
    if ch == '\n':
        c+=1
    ch=fo.read(1)
print("Total number of lines : ",c)

#5) write in the file f2.txt

fo=open("f2.txt",'w')#file will be created automatically
fo.write("Hey")
fo.write("Viraj")
fo.write("Rubaba")
fo.close()


#6) append in the file f2.txt

fo=open("f2.txt",'a')#try with 'w' also
fo.write("How are you all?")
fo.close()





#7) count number of words
#8) count the words starting with 't'


'''

#9) count number of lines

fo=open("f2.txt")
L=fo.readline()#read a line with \n(EOL)
print(L.rstrip())#remove any whitespace from right end
L=fo.readline()#read a line with \n(EOL)
print(L,end="")

fo=open("f2.txt")
L=fo.readline()#read a line with \n(EOL)
c=0
while L:#if L is existing
    c+=1
    L=fo.readline()
print("Total number of lines : ",c)

fo=open("f1.txt")
L=fo.readlines()#read all the lines with \n at the end and put in the list
print(L)
print("Total number of lines =",len(L))


# count the lines starting with 'the'
fo=open('f1.txt')
L=fo.readline()
c=0
while L:
    if L.startswith("the"):
        c+=1
    L=fo.readline()
print(c)
fo.close()    

# count the  'the' in the file

fo=open("f1.txt")
fo2=open("f5.txt",'a')
L=fo.readline()
c=0
while L:
    Li=L.strip().split()#L.strip().split()= ['hello', 'the' ,'to' ,'the' ,"rock"]
    for w in Li:
        if w=='the':
            c+=1
    if len(Li)>5:
        fo2.write(L)        
    L=fo.readline()
print(c)
'''


