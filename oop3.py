#classes
# customer-> names, email, kra, dob, gender
#bankAccount-> Customer, acc_no, acc_type, balance

class Customer:
    def __init__(self, names:str, email:str, kra:str, dob:str, gender:str):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender
    def define_details(self):
        print(f"Name : {self.names} and KRA PIN : {self.kra} ")

    def __str__(self):
        return f"{self.names} {self.gender}"

class Account:
    def __init__(self, owner:Customer, acc_no:str, acc_type:str, balance:float ):
        self.acc_no = acc_no
        self.owner = owner
        self.acc_type = acc_type
        self.balance = balance
    def print_details(self):
        print(self.owner.names)
        print(self.acc_type)
        print(self.balance)
        print(self.acc_no)



    def deposit(self, amount:float):
        self.balance += abs(amount)
    def withdraw(self, amount:float):
        if amount > self.balance:
            print("Refill Account Fala HII")
        else:
            self.balance -= abs(amount)
    def __str__(self):
        return f"Account No{self.acc_no} {self.owner.names}"


Kenya1 = Customer("Jimi James", "me@email.com", "KRA1843A5T6", "21-2-2027","male")
imagineJ = Customer("Mercy Monkey", "momkey@email.com", "KRA1443S7T6", "26-12-2022","female")

acc1 = Account(Kenya1, "12004672883", "current", 273_722_992)
acc2 = Account(Kenya1, "120044466", "savings", 2_737_229)
acc3 = Account(imagineJ, "1204446", "savings", 37_229)

# print(Kenya1.dob)
# print(Kenya1.show_details())

acc1.print_details()
acc1.deposit(102333)
acc1.print_details()
acc1.withdraw(1023330000)
acc1.print_details()

print(acc1.owner)
