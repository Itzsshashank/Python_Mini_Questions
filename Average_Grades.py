class Students:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

example_grades = [90, 85, 92, 78, 95]

student = Students("Shashank", 18, example_grades)

print("Average Grade:", student.average_grade())
