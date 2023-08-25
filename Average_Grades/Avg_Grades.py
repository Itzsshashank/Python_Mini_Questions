class Employee:
    def __init__(self, name, position, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def raise_salary(self, percentage):
        increase = (percentage / 100) * self.salary
        self.salary += increase

percentage1 = 10
employee = Employee("Shashank", "CEO", 100000)
employee.raise_salary(percentage1)
print(f"{employee.name} is a {employee.position} with a salary of Rupees: {employee.salary}")
