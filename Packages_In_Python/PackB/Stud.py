class Student:
    def __init__(self, sName, sId, sMarks):
        self.sName=sName
        self.sId=sId
        self.sMarks=sMarks

    def show(self):
        print(self.sName,self.sId,self.sMarks)

        