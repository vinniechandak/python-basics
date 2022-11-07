# this file is about strings #
values = {'vegetable': 'Bhindi', 'roti': 'Tandoori'};
s = 'I like %(vegetable)s and %(roti)s togather.' % values;
print(s);

a = 'This is a Single Quote String.'
b = "This is a double Quote String."
c = """This string is spread across multiple lines.
	Don't you believe this ??
	Check then :P"""
d = a + " " + b
print(a);
print(b);
print(c);
print(d);

# example of translate.
import string;

a = 'Vinod Chandak';
print(a);
print(a.maketrans("chandak", "CHANDAK"));
