class bolwer:
    def __init__(self,fname,lname,oversbowled,noofmaidenovers,runsgiven,wicketstaken):
        self.fname=fname
        self.lname=fname
        self.oversbowled=oversbowled
        self.noofmaidenovers=noofmaidenovers
        self.runsgiven=runsgiven
        self.wicketstaken=wicketstaken
    def update(self,a,b,c,d,e,f):
        self.fname=a
        self.lname=b
        self.oversbowled=c
        self.noofmaidenovers=d
        self.runsgiven=e
        self.wicketstaken=f
        print "successfully updated"
    def display(self):
        print self.fname,self.lname,self.oversbowled,self.noofmaidenovers,self.runsgiven,self.wicketstaken

a1=bolwer(raw_input("enter the  first name"),raw_input("enter the  second name"),int(raw_input("enter n0. of overs bowled")),int(raw_input("enter n0. of maiden overs")),int(raw_input("enter n0. of runs given")),int(raw_input("enter n0. of wickets taken")))
choice=raw_input("do u want to update? if yes type yes else no")
if choice=="yes":
    print "plz enter the info below"
    a1.update(raw_input("enter the  first name"),raw_input("enter the  second name"),int(raw_input("enter n0. of overs bowled")),int(raw_input("enter n0. of maiden overs")),int(raw_input("enter n0. of runs given")),int(raw_input("enter n0. of wickets taken")))
else :
    print ".............."
