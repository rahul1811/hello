no = 0
length = 0
count = 0
f = open('student.txt','r')
for i in f.readlines() :
    print i
    no+= 1
    b= len (i)
    length += b
    a = i.split(' ')
    for j in a:
        if j[0] == "A":
            count += 1
print "no. of capital a present",count
print "no. of character",length
print "no. of lines",no
