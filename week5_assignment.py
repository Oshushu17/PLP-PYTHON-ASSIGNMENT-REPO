class Employee():
    def __init__(self, name, qualification, work_at):
        self.name = name
        self.qualification = qualification
        self.work_at = work_at
    def get_employee(self):
        return f"my name is {self.name}. I work at {self.work_at} and hold a degree in {self.qualification}"

employer = Employee("Mike", "BSc Computer Science", "plp")
print(employer.get_employee())

class Savings(Employee):
    #Initializing Savings constructor along with parent attributes
    def __init__(self, name, qualification, work_at):
        self.__amount_saved = 160  #private attribute for encapsulation
        super().__init__(name, qualification, work_at) # Bringing in Parent

    def me(self):
        #using parent method
        return super().get_employee()
        
    def saving_amount(self):
        salary = 200
        if self.__amount_saved <0:
            return f"amount cannot be {self.__amount_saved}"

        elif self.__amount_saved < salary:
            deduct = 0.2 * salary
            total_savings = deduct + self.__amount_saved
            return f"# {total_savings}"
        else:
            return "salary too small to be deducted from"

my_savings = Savings("Steve", "BSc Accounting", "Google")
my_savings.me()
print(my_savings.saving_amount())


class Car:
    def move(self):
        return "driving"
    
class Boat:
    def move(self):
        return "sailing"
    
class Bicycle:
    def move(self):
        return "riding"

class Jet:
    def move(self):
        return "flying"

for movement in [Car(), Boat(), Bicycle(), Jet()]:
    print(movement.move())