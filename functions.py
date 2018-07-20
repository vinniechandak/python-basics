# This file includes functions in python.

def mytest():
    print('This is test function.')


a = lambda x: x ** 2;
print("Printing Lambda:", a);

print("Lambda Function call:", a(4));


def function_def_arg(x=5):
    print("Value of x:", x);


# calling functions.
function_def_arg();
function_def_arg(4);


def function_arg_order(x, y=3, *z, **p):
    print("Value of x:", x);  # This is compulsory argument.
    print("Value of y:", y);  # This is optional argument with default value.
    print("Value of z:", z);  # Printing lists and tuples.
    for item in z:
        print("Value of item in args:", item);
    print("Value of p:", p);  # Printing dictionary arguments.
    for key, item in p.items():
        print("Key of dictionary:", key);
        print("Value of dictionary:", item);


# calling function
function_arg_order(5, 9, 'aa', 'bb', 'cc', a=5, b=6);


def function_return_multiple_values(x, y):
    return x * 2, y * 3;


# calling function
a, b = function_return_multiple_values(2, 3);
print("Return Value of first:", a);
print("Return Value of second:", b);
