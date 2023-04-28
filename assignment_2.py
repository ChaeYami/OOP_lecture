class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        pass
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
    
    def speak(self):
        print("멍")
        
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
    
    def speak(self):
        print("냥")
        
my_sweetie = Cat('cutie','2')
my_sweetie.speak()