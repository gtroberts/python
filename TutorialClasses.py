class MyClass:
    """Simple class"""
    
    i = 12345
    
    def f(self):
        return "MyClass:f"
        
        
x = MyClass
print(x)
print(x.i)
print(x.f())