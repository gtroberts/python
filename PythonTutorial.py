# Keyword arguments

def f1(a, b=5):
	return a + b
	
print(f1(1), "Should be 6")
print(f1(1, 2), "Should be 3")
print(f1(b=2, a=1), "Should be 3")



def f2(a, *args, **kwargs):
	print(a)
	for arg in args:
		print("Arg:", arg)
	keys = sorted(kwargs.keys())
	for kwarg in keys:
		print("Kwarg:", kwarg)

f2("hello", "This", "is", "a", "list", of="of", keyword="keyword", arguments="arguments")

# Lamba expressions

def sort_by_value(map):
	map.sort(key=lambda pair:pair[1])
	
map = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]

print(map)
sort_by_value(map)
print(map)


def do(f, a, b):
	return f(a, b)

a, b = 2, 3
print(a, "+", b, "=", do(lambda x, y: x + y, a, b))
print(a, "*", b, "=", do(lambda x, y: x * y, a, b))
print(a, "/", b, "=", do(lambda x, y: x / y, a, b))

def make_doer(a, b):
	return lambda f: do(f, a, b)
	
doer = make_doer(a, b)

import operator

print(a, "+", b, "=", doer(operator.add))
print(a, "*", b, "=", doer(operator.mul))
print(a, "/", b, "=", doer(operator.truediv))
