#2. Class syntax
class Animal(object):
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)

#8.-9.
class Animales(object):
    """Makes cute animals."""
    is_alive = True
    health = 'good'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print (self.name)
        print (self.age)
        
hippo = Animales('Humphrey', 5)
sloth = Animales('Molly', 3)
ocelot = Animales('Julio', 4)

print (hippo.health)
print (sloth.health)
print (ocelot.health)

#10.
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added.")
        else:
            print (product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in the cart.")
            
my_cart = ShoppingCart('Jefe')
my_cart.add_item('pussy', 100)
#11. Inheritance
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#12.
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

#13.-14. Override 
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
    
milton = PartTimeEmployee('Milton')
print (milton.full_time_wage(33))
    
pt = PartTimeEmployee('Julio')
ft = Employee('Julia')

####easier example below
class Empl(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print ("Hello, %s" % other.name)

class CEO(Empl):
    def greet(self, other):
        print ("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Empl("Steve")
emp.greet(ceo)
ceo.greet(emp)

#14-18 Review
class Triang(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
        
class Equilateral(Triang):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
            
my_triangle = Triang(60,40,80)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())  

#Car 1-10
class Car(object):
    condition = 'new'
    print
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        
    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + "MPG."
    
    def drive_car(self):
        self.condition = "used"
        
class ElectricCar(Car):
    def __init__(self, model,color,mpg,battery_type):
            super(ElectricCar, self).__init__(model,color,mpg)
            self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"
        
            
my_car = ElectricCar(model = "DeLorean", color = "silver", mpg = 88, battery_type = "molten salt")
print (my_car.condition)
my_car.drive_car()
print (my_car.condition)
#Car 11
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "(%d ,%d, %d)" % (self.x, self.y, self.z)
    
    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)
print (my_point)
print (bin((0b101 & 0b111) | 0b1001))
print (bin(20))
