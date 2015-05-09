# This file contains operation related to file.
f = open('myfile.txt', 'w');
f.write('This is a text message inside a file.'); # writing content to file.
f.close();
print f;

with open('myfile.txt', 'r') as content: # reading data from existing file.
	for data in content:
		print data;