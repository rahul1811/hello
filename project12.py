class traininfo:
    def __init__(self):
        self.tname=""
        self.tno=0
        self.deptime=""
        self.boarding=""
        self.destination=""
        self.nosT1=0
        self.nosT2=0
        self.nosT3=0
 
    def indata(self):
        self.tname=raw_input("enter the train name")
        self.tno=int(raw_input("enter the train number"))
        self.deptime=raw_input("enter the train deoarture time")
        self.boarding=raw_input("enter the train boarding ")
        self.destination=raw_input("enter the train destination")
        self.nosT1=int(raw_input("enter the total seats"))
        self.nosT2=int(raw_input("enter the total seats"))
        self.nosT3=int(raw_input("enter the total seats"))
 
    def display1(self):
        print "train name : ",self.tname
        print "train number : ",self.tno
        print "train departuretime : ",self.deptime
        print "train boarding: ",self.boarding
        print "train destination : ",self.destination
        print "train seats in T1 : ",self.nosT1
        print "train seats in T2 : ",self.nosT2
        print "train seats in T3 : ",self.nosT3

    def infoin(self):
        fin=open("traininfo.txt" , "a" )
        num=int(raw_input(" Enter the number of trains you want to enter "))
        for i in range(num):
            self.indata()
            pickle.dump(self,fin)
            print " data enrolled in file "
s= traininfo()
s.infoin()
class boarding(traininfo):
    def __init__(self):
        traininfo.__init__(self)
        self.tname=""
        self.tno=0
        self.date=""
        self.avseatsT1=traininfo.nosT1
        self.avseatsT2=traininfo.nosT2
        self.avseatsT3=traininfo.nosT3
 
 
    def indata2(self):
        self.tname=raw_input("enter the train name")
        self.tno=int(raw_input("enter the train name"))
        self.date=raw_input("enter the date")

 
    def display2(self):
        print "train name : ",self.tname
        print "train number : ",self.tno
        print "train available dates : ",self.date
        print "train avseats in T1: ",self.avseatsT1
        print "train  avseats in T2: ",self.avseatst2
        print "train  avseats in T3: ",self.avseatst3
       
class reservation:
    def __init__(self):
        self.tname=""
        self.date=""
        self.reqseats=0
 
    def indata3(self):
        self.tname=raw_input("enter the train name")
        self.date=raw_input("enter the date")
        self.reqseats=print "train name : ",self.tname
       
 
   def display3(self):
        print "train name : ",self.tname
        print "train available dates : ",self.date
        print "required trains are:",self.reqseats

 
def userinfo:
    def __init__(self):
        self.username=""
        self.age=0
        self.adharno=0
 
    def indata3(self):
        self.tname=raw_input("enter the user name")
        self.date=raw_input("enter the age")
        self.adharno=int(raw_input("enter the adharno"))
       
 
   def display3(self):
        print "user name : ",self.username
        print " age : ",self.age
        print "adharno :",self.adharno

