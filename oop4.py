#inheritance

#employee-> name, id_no, department, gender
#salaried -> salary, tenure
#casula->rates,
#parent-class
class Employee:
    def __init__(self, name:str, id_no:str, department:str, gender:str):
        self.full_name = name
        self.identity_no = id_no
        self.department = department
        self.gender = gender

    def print_details(self):
        print(self.full_name)
        print(self.identity_no)
        print(self.department)
        print(self.gender)
        print("----------------------")


    def print_name(self  ):
        print(f"Name is {self.full_name}")

#subclass/child
class SalariedEmployee(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str,salary:int, tenure:int):
        super().__init__(name, id_no, department, gender)
        self.tenure = tenure
        self.salary = salary

class CasualWorkers(Employee):
    def __init__(self, name:str, id_no:str, department:str, gender:str, rate:int):
        super().__init__(name, id_no, department, gender)
        self.rate = rate

    def calc_wage(self, hours:float  ):
        return hours * self.rate

s1 = SalariedEmployee("Elizabeth Susan", "24553344", 'HR', "F", 35_333, 3)
c1 = CasualWorkers("Jack Daniels", "46387464", "Sales","M",44)
s1.print_details()
c1.print_details()
print(c1.calc_wage(40))


c1.print_name()

#create your own branch
#command used to create new branch#
#you can write some code to test your code
