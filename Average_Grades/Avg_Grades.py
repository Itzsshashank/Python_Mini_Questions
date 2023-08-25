class Students:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

# Example grades as a list of numbers
example_grades = [90, 85, 92, 78, 95]

# Create an instance of the Students class
student = Students("Shashank", 18, example_grades)

# Call the average_grade method and print the result
print("Average Grade:", student.average_grade())
