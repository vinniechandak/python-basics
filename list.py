# Python Lists

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
print
a;

b = range(0, 9);
print
"Using Range:", b;

c = a[2:6];  # included initial indexed element but not the last index position element.
print
"Sliced List:", c;

d = a[-5:-1];  # starts index in reverse order starting from -1.
print
"Negative Index Slice :", d;

e = a + b;  # appends list b to list a;
print
"Addition of List : ", e;

f = a * 3;  # appends same list n times where n is multiplier.
print
"Multiplication :", f;

g = a[::2];  # slices the list with the span of specified number.
print
"Slicing with Strides:", g;

h = a.append(
    'new element');  # inserts element at the last index. To add at specific index use insert(index, item) function.
print
"Append Element:", a;

i = b.pop();
print
"Pop Element:", i, "Remaining List : ", b;

j = a.extend(b);
print
"Extending List:", j;

l = ["a", "b", "c"];
k = '|'.join(l);
print
"Joining List:", k;
