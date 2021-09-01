from abc import ABC, abstractmethod

# Parent Class
class Employee(ABC):
    def payStub(self, amount):
        print("Your gross paycheck is: ", amount)
    # Here is an abstract method
    @abstractmethod
    def payment(self, amount):
        pass

# Child Class
class Employee_Payroll(Employee):
    # Here I define the abstract method from my parent class Employee
    def payment(self, amount):
        print('Your gross paycheck amount of {} will be directly deposited to your primary financial institution.'.format(amount))

obj = Employee_Payroll()
obj.payStub("$1,800")
obj.payment("$1,800")