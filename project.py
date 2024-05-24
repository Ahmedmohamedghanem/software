#Design_Pattern
#.................
# Creational Patterns
#................
#Factory

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("Invalid shape type")

# Define the Circle, Rectangle, and Triangle classes
class Circle:
    pass

class Rectangle:
    pass

class Triangle:
    pass

shape_factory = ShapeFactory()
circle = shape_factory.create_shape("circle")
rectangle = shape_factory.create_shape("rectangle")
triangle = shape_factory.create_shape("triangle")

#.........................................
#Structural patterns
#Decorators
class Pizza:
    def get_description(self):
        pass

    def get_cost(self):
        pass

class Margherita(Pizza):
    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 8.99

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class ExtraCheese(PizzaDecorator):
    def get_description(self):
        return super().get_description() + ", Extra Cheese"

    def get_cost(self):
        return super().get_cost() + 1.99

margherita = Margherita()
margherita_with_extra_cheese = ExtraCheese(margherita)
#.........................................
#Behavioral patterns
#Observer

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        pass

class ConcreteObserver(Observer):
    def update(self):
        print("Update received")

subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()

#.................................................................................
#Solid_Principle
#...........
# SRP_Violation

class Person:
    def __init__(self, name): 
        self.name = name
    def __repr__(self):
        return f'Person(name={self.name})'
    @classmethod
    def save(cls, person): 
        print(f'Save the {person} to the database')
if __name__ == '__main__':
    P = Person ('John Doe')
    Person.save(p)
    
# SRP_Solution

class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self): return f'Person(name={self.name})'
class PersonDB:
    def save(self, person): 
        print(f'Save the (person) to the database')
if __name__ == '__main__':
    P = Person('John Doe')
    db = PersonDB()
    db.save(p)
#......................................................................................

# OCP_Violation

from math import pi
class Shape:
    def _init__(self, shape_type, kwargs):
        self.shape_type =shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height= kwargs["height"]
        elif self.shape_type == "circle":
            self.radius =kwargs["radius"]
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
            
from shapes_ocp import Shape
rectangle= Shape("rectangle", width=10, height=5)
rectangle.calculate_area()
50
circle =Shape("circle", radius=5)
circle.calculate_area()
78.53981633974483    

#OCP_Solution

from abc import ABC, abstractmethod 
from math import pi
class Shape (ABC):
    def _init__(self, shape_type): 
        self.shape_type = shape_type
    @abstractmethod
    def calculate_area(self): pass
    
class Square (Shape):
    def _init__(self, side): 
        super()._init__("square")
        self.side= side
    def calculate_area(self): 
        return self.side**2
class Rectangle (Shape):
    def _init__(self, width, height): 
        super()._init_("rectangle") 
        self.width = width 
        self.height =height
    def calculate_area(self): 
        return self.width* self.height    
class Circle(Shape):
    def _init_(self, radius): 
        super()._init__("circle") 
        self.radius = radius
    def calculate_area(self): 
        return pi *self.radius** 2        
#...........................................................................        
#LSP_Violation

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message, recipient):
        pass

class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')

class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

if __name__ == "__main__":
    contact = Contact("John Doe", "john@test.com", "(408)-888-9009")
    notification_manager = NotificationManager(SMS(), contact)
    notification_manager.send("Hello")


# LSP_solution

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send '{message}' to {self.email}")

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send '{message}' to {self.phone}")

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)

if __name__ == "__main__":
    contact = Contact("John Doe", "john@test.com", "(488)-888-9999")
    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("Hello John")

    notification_manager.notification = email_notification
    notification_manager.send("Hi John")

#..........................................................................
#ISP_Violation

from abc import ABC, abstractmethod

class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):

    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):

    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

# Usage Example
if __name__ == "__main__":
    old_printer = OldPrinter()
    modern_printer = ModernPrinter()

    # Using OldPrinter
    old_printer.print("Document1")
    try:
        old_printer.fax("Document1")
    except NotImplementedError as e:
        print(e)
    try:
        old_printer.scan("Document1")
    except NotImplementedError as e:
        print(e)

    # Using ModernPrinter
    modern_printer.print("Document2")
    modern_printer.fax("Document2")
    modern_printer.scan("Document2")

#ISP_solution

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
#...............................................................................
#DIP_Violation

class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")

class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)

if __name__ == "__main__":
    app = App()
    app.start()

#DIP_Solution

from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_currency, amount) -> float:
        pass

class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 2

class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)

if __name__ == "__main__":
    app = App(FXConverter())
    app.start()
#...............................................................................
#Architecture patterns
#MVC
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# View
class UserView:
    def display_user_details(self, username):
        print(f"Username: {username}")

# Controller
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user_details(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.model(username, password)
        self.view.display_user_details(user.username)  # Pass the username attribute
#....................................................................        