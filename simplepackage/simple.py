# simple.py file which can be imported to other files
import sys
def test_sum(a, b):
	print a+b;

if __name__=='__main__':
	test_sum(int(sys.argv[1]), int(sys.argv[2]));