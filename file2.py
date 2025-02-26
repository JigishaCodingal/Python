'''
#1)read a line from file
fo=open("f1.txt")
L=fo.read()#read entire file content
print(L)
L=fo.read(5)#read only 5 characters of file content
print(L)
L=fo.readline()#read a line
print(L)
fo.close()
#2)read 3 lines
fo=open("f1.txt")
for i in range(3):
    L=fo.readline()#read a line with \n(enter key/ new line character)
    print(L)

#read, write and append
#'r' : read(): 1 character
#readline()
#3) count and display all the lines of file
fo=open("f1.txt")#read mode
L=fo.readline()  #1st line
#line is read with \n(new line char/enter key) at the end
c=0
while L:#line is existing
    c=c+1#1,2
    print(L.rstrip())#line has \n at the end+ print
    L=fo.readline()#next line

#4) display only odd lines
fo=open("f1.txt")
L=fo.readline()
#line is read with \n(new line char/enter key) at the end
c=0
while L:
    c=c+1
    if c%2!=0:
        print(L.rstrip())
    L=fo.readline()

#5) take only odd lines in another file
fr=open("f1.txt")#read mode
fw=open("f11.txt",'w')#write mode
L=fr.readline()
#line is read with \n(new line char/enter key) at the end
c=0
while L:
    c=c+1
    if c%2!=0:
        fw.write(L)
    L=fr.readline()
fr.close()
fw.close()

#6) take only those lines which start with 't'
fr=open("f1.txt")#read mode
fw=open("f11.txt",'w')#write mode
L=fr.readline()
#line is read with \n(new line char/enter key) at the end
while L:
    if L.startswith('t'):
        fw.write(L)
    L=fr.readline()
fr.close()
fw.close()


#7) count the number of words in each line
fo=open("f1.txt")#file opened in read
L=fo.readline()#one line 
#line is read with \n(new line char/enter key) at the end
c=0
while L:
    c=c+1
    Li=L.split()#[hello, how, are, you?]
    print("Line",c,"Total number of words = ",len(Li))
    L=fo.readline()

#ACP) take only those lines which contain 'the' inside it into another file

#8)display the longest word from each line
fo=open("f1.txt")
L=fo.readline()
#line is read with \n(new line char/enter key) at the end

while L:
    Li=L.split()#[hello, how, areyou?,he]
    x=0  #to store length of word
    for w in Li:
        y=len(w)#5, 3, 7
        if y>x:#0
            x=y  #5, 7
            w1=w  #hello, areyou?
        
    print("longest word in",L,"is",w1,"with",x,"characters\n\n")
    L=fo.readline()

#9) delete a file and folder
import os
if os.path.exists('f11.txt'):
    os.remove('f11.txt')
else:
    print("file does not exist")

os.rmdir('Demo')

'''
#10)remove duplicate lines from file
fo=open('f2.txt')
fi=open('f3.txt','w')
L=fo.readline()#abc
L1=[]
while L:
    if L not in L1:
        L1.append(L)#abc,def
    L=fo.readline()#def, abc
fi.writelines(L1)
fo.close()
fi.close()
import os
os.remove('f2.txt')
os.rename('f3.txt','f2.txt')


