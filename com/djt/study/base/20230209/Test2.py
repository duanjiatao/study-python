class Student:
    """first python class"""

    # field
    name = "no"
    age = 10

    def __int__(self):
        pass

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # function
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


zhangsan = Student
print(f"name={zhangsan.name} age={zhangsan.age}")
lisi = Student("lisi", 30)
print(f"name={lisi.name} age={lisi.age}")
