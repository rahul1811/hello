import pickle
class student(object):
	def __init__(self):
		self.rollno = 0
		self.name = " "
	def getdata(self):
		self.rollno = int(raw_input("enter roll no."))
		self.name =raw_input("enter name")
	def printdata(self):
		print "roll no" , self.rollno
		print "name", self.name
class marks(student):
    def __init__(self):
        student.__init__(self) 
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
        self.n5 = 0
    def inputdata(self):
        student.getdata(self)
        self.n1 = int(raw_input("enter marks in physics"))
        self.n2 = int(raw_input("enter marks in eng"))
        self.n3 = int(raw_input("enter marks in chem"))
        self.n4 = int(raw_input("enter marks in cs"))
        self.n5 = int(raw_input("enter marks in maths"))
    def outdata(self):
        print self.n1
        print self.n2
        print self.n3
        print self.n4
        print self.n5
a2 = student()
a2.getdata()
a2.printdata()   
a2 = marks()
a2.inputdata()
a2.outdata()
    
file1 = open ("student1.log","wb")
pickle.dump(a2,file1)
file1.close()
    
