from typing import List, Dict

class MyClass:
    x = 5
    

obj = MyClass()
# del obj
print(obj.x)

class MySecondClass:
    
    def __init__(self,name,age = 25):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)

obj = MySecondClass("suriya")

obj.show()

class MyThirdClass:
    pass
    def agePlus(thisObj):
        thisObj.age = 50
obj = MyThirdClass()
obj.name = "suriyaa"
obj.age = 255

print(obj.name,obj.age)

obj.age = 30

obj.agePlus()
print(obj.name,obj.age)

class Calculator:

    def add(self,a,b):
         return a + b

    def multiply(self,a,b=11):
         return a * b
    
    def printAll(self):
        print(f"{self.add(1,1)},{self.multiply(4,6)}")

obj = Calculator()
obj.printAll()

class Person:
     def __init__(self,f_name,l_name):
         self.f_name = f_name
         self.l_name = l_name

class Student(Person):
    pass

obj = Student("s","p")
print(obj.f_name)



# tasks started
class Student:
    
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"age : {self.age}")
        print(f"course : {self.course}")
obj = Student("suriya",25,"AI ENGINEER")
obj.display_info()



class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self,amount):
        self.balance = self.balance + amount
        print(f"D current Balance : {self.balance}")

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f"W current Balance : {self.balance}")


    def check_balance(self):
        print(f"Account Holder Name : {self.account_holder} , Balance : {self.balance}")

obj = BankAccount("suriya",0)
obj.check_balance()
obj.deposite(1000)
obj.check_balance()
obj.withdraw(200)
obj.check_balance()
obj.deposite(10000)

class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")


class Cat(Animal):

    def speak(self):
        print("Cat meows")


# Create objects
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        self.__salary = salary 

obj = Employee(20000)

obj.set_salary(30000)
print(obj.get_salary())

class Product:
    def __init__(self,products):
        self.products = products

    def add_product(self,product):
        self.products.append(product)
    
    def delete_product(self,product):
        for pro in self.products:
            if pro["name"] == product["name"]:
                pro.get()
                self.products.remove(pro)
        
products = [{"name":"mobile","price":1000,"quantity":10},
            {"name":"laptop","price":2000,"quantity":20},
            {"name":"tablet","price":3000,"quantity":30}]

obj = Product(products)
new_product = {"name": "watch", "price": 500, "quantity": 5}
new_product.get()
obj.add_product(new_product)
obj.delete_product(new_product)
print(obj.products)