#This is about dictionary data structure in python.
d = {'a':'b', 'c':'d', 'e':'f'};
print d;

d['Vinod'] =  'Chandak'; # appending element to dictionary
print d;

d['a'] = 'Modified key a'; # value overriding.
print d;


print d.items(); # print items of a dictionary in a tuple format.
print d.keys(); # print keys of a dictionary. 
print d.values(); # print values of a dictionary.

print d.has_key('a');  # checking whether key exists in dictionary or not.
print d.get('Vinod');  # get value by key. if key doesn't exists it returns None.
