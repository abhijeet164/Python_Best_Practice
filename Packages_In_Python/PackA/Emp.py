class Employee:
    def __init__(self,enam ,eid,esal):
        self.enam = enam
        self.eid = eid
        self.esal = esal
    def display(self):
        print(self.enam,self.eid,self.esal)