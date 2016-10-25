class MyClass:
    """Simple class"""
    
    def __init__(self):
        print("MyClass.__init__")

    i = 12345
    
    numbers = []
    
    def f(self):
        print("MyClass.f")
        
    def x(self):
        print("MyClass.x")
        
    def setName(self, name):
        self.name = name
    
    def addNumber(self, i):
        self.numbers.append(i)    
        
        
x = MyClass()
print(x)
print(x.i)
x.f()

y = MyClass()

x.j = x.i * x.i
y.j = y.i * y.i

print("x.j", x.j, "y.j", y.j, "should be same")

# method object

xf = x.f

xf()

#  class / instance variables

a = MyClass()
b = MyClass()

a.setName("a")
b.setName("b")
a.addNumber(100)
b.addNumber(200)

print("a", a.name, a.numbers)
print("b", b.name, b.numbers)

b.numbers = []

print("a", a.name, a.numbers)
print("b", b.name, b.numbers)

a.addNumber(300)
b.addNumber(400)

print("a", a.name, a.numbers)
print("b", b.name, b.numbers)


# inheritance

class MyDerivedClass(MyClass):
    """Derived Class"""

    def f(self):
        print("MyDerivedClass.f")
        
    def g(self):
        print("MyDerivedClass.g")
        MyClass.f(self)
        
    def setName(self, name):
        MyClass.setName(self, name) 
        
    def x(self):
        print("MyDerived.x")
        

            
d = MyDerivedClass()
d.f()
d.g()
d.setName("Derived")
print(d.name)

print("isinstance(b, MyClass)", isinstance(b, MyClass))
print("isinstance(b, MyDerivedClass)", isinstance(b, MyDerivedClass))
print("isinstance(d, MyClass)", isinstance(d, MyClass))
print("isinstance(d, MyDerivedClass)", isinstance(d, MyDerivedClass))

print("issubclass(MyDerivedClass, MyClass)", issubclass(MyDerivedClass, MyClass))
print("issubclass(MyClass, MyDerivedClass)", issubclass(MyClass, MyDerivedClass))

# diamond

class MyDerivedClass2(MyClass):
    """Another Derived Class"""
    
    def f(self):
        print("MyDerivedClass2.f")

    def x(self):
        print("MyDerivedClass2.x")
        
class JoinClass(MyDerivedClass, MyDerivedClass2):
    """join class"""
    
    def f(self):
        print("JoinClass.f")
        MyDerivedClass.f(self)
        MyDerivedClass2.f(self)
        MyClass.f(self)

    def y(self):
        print("JoinClass.y")
        self.x()    # calls MyDerivedClass.x
       
    
j = JoinClass()
j.f()
j.y()