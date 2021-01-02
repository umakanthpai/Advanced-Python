from datetime import date 
   
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    def __str__(self):
      return f"name: {self.name} age: {self.age}"

       
    # a class method to create a Person object by birth year. 
    # Method gets cls, can change a class variable for every instance
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
       
    # a static method to check if a Person is adult or not. 
    # Nothing special, should be used like utlity method
    @staticmethod
    def isAdult(age): 
        return age > 18
   
