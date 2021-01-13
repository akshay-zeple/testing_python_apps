print("Hello World!!")


class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay


    @classmethod
    def global_hike(cls, emp):
        return cls(emp.name, emp.pay + 1000)


emp = Employee("Akshay", 5000)
emp_new = Employee.global_hike(emp)

print(emp.pay)
print(emp_new.pay)