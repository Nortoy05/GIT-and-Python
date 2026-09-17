'''Class

1->What is class
2->ordinary vs static properties
3->special methods

'''

print("=========== What is class =================")

#structure-> state, consturctor ,method


class Person():
    #state
    message="class state property"

    #constructor
    def __init__(self, name, age):
         self.name=name
         self.age=age

#method
    def introduce(self):
        print(f" the  {self.name} says: How do you do ?")


    def say_age(self):
         print(f" {self.name} says  I am {self.age}")

    @classmethod
    def explain():
         print("Static method property is executed")




person1 =Person("Justin",25)
person2=Person("Ethan",21)
person3=Person("John",22)

print("person1.name: ",person1.name)

person1.introduce()
person2.say_age()


print("=========== ordinary vs static properties =================")

new_message=Person.message
print("new_message: ", new_message)


print("=========== special methods =================")

# __init__ , __new__, __str__, __getitem__, __eq__, __len__ ....


class Car():
     #state
     desciption="This class makes cars"

     def __new__(cls, *args):
          print("*  __new__ *")
          return super().__new__(cls)

     #constructor
     def __init__(self, name, year):
         self.name=name
         self.year=year



     #method
     def start_engine(self):
          print(f"the {self.name} started engine!")

     def stop_engine(self):
               print(f"the {self.name} stopped engine!")

     def __str__(self):
          return f" the car.name {self.name} was produced in {self.year} year!"

     def __call__(self, *args, **kwds):
          print("Object is called as function!")


my_car =Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()


your_car =Car("Toyota", 2025)
print(your_car)

response=your_car()