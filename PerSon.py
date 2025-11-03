class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        return f"name:{self.name} \nage:{self.age}"
    
person1 = Person("ali",19)
print(person1.display())


class Student(Person):
    def __init__(self, name, age,major):
        super().__init__(name, age)
        self.major = major
    def display(self):
            return f"student name:{self.name} \nstudent age & major:{self.age , self.major}"
    
student1 = Student("zahra",16,"vet")
print(student1.display())
