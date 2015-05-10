# loop structure in python

a = [1,2,3,4,5,6,7,8,9,0];

for item in a:
	print item;
count = 0;
while(count<10):
	print a[count];
	count = count+1;

for index, item in enumerate(a):
	print index,". ", item;
