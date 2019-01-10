class emp:
    """emp app"""
    empcount=0
    def __init__(self,empname,empadd,empid,empsal):
        self.empname=empname
        self.empadd=empadd
        self.empid=empid
        self.empsal=empsal
        emp.empcount=emp.empcount+1
    def __del__(self):
        emp.empcount=emp.empcount-1
    def display (self):
        print(self.empname)
        print(self.empadd)
        print(self.empid)
        print(self.empsal)
      
e1=emp("bharath","hyd",1001,10000.00)
e2=emp("sai","gnt",1002,20000.00)
e3=emp("satyam","sap",1003,30000.00)
e1.display()
e2.display()
e3.display()
del e1
del e2
del e3

print("total no of employees are",emp.empcount)
