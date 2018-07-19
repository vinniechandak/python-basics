# This is about dictionary data structure in python.
d = {'a': 'b', 'c': 'd', 'e': 'f'};
print("Print Dictionary ==> " , d);

d['Vinod'] = 'Chandak';  # appending element to dictionary
print("Print Amended Dictionary ==> " , d);

d['a'] = 'Modified key a';  # value overriding.
print("Print Value Overridden Dictionary ==> ",d);

print("Print Dictionary as a Tuple ==> " , d.items());  # print items of a dictionary in a tuple format.
print("Print Dictionary Keys ==> " ,d.keys());  # print keys of a dictionary.
print("Print Dictionary Values ==> " ,d.values());  # print values of a dictionary.

print("Print Dictionary Contains Key? ==> " ,d.__contains__('a'));  # checking whether key exists in dictionary or not.
print("Print Dictionary Value by Key ==> " ,d.get('Vinod'));  # get value by key. if key doesn't exists it returns None.
