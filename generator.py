def simplegen():
    yield 'aaa'
    yield 'bbb'
    yield 'ccc'


a = simplegen();
print(a);
for item in a:
    print(item)

# a generator for generating element, square and cube of the element
a = [lambda x: x,
     lambda x: x ** 2,
     lambda x: x ** 3]

print(a[0](3));
print(a[1](3));
print(a[2](3));
