class cust:
    "banking app"
    cbname="boi"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def deposit(self,damt):
        self.damt=damt
        self.cbal=self.cbal+damt
    def withdraw(self,wamt):
        self.wamt=wamt
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
customer=cust("bharath","hyd",10000,20000.00)
print(customer)
customer.deposit(2000)
customer.display()
print("-----------------")
customer.withdraw(5000)
customer.display()
print("-----------------")
c2=cust("bharath","hyd",10000,20000.00)
print(c2)
customer.deposit(1000)
customer.display()
print("-----------------")
customer.withdraw(2000)
customer.display()
print("-----------------")
c3=cust("sai","vjd",1001,10000.00)
print(c3)
customer.deposit(2000)
customer.display()
print("-----------------")
customer.withdraw(5000)
customer.display()
        
    
