class student:
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade
    def display(self):
        print(f"Name of the stuent is {self.name} and grade is {self.grade}")

student1=student("chinmay", "A+")
student2=student("Ruchitha(mau)", "A++")

student1.display()
student2.display()