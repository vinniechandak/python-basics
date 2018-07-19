# conditional statements in python
import sys as sys

a = int(sys.raw_input("Enter value 1:"));
b = int(sys.raw_input("Enter value 2:"));

print("""Enter Choice:
1. sum
2. subtract
3. multiply
4. division
5. modulus""")

choice = int(sys.raw_input());

if choice == 1:
    print("Sum:", a + b);
elif choice == 2:
    print("Subtraction:", a - b);
elif choice == 3:
    print("Multiplication:", a * b);
elif choice == 4:
    print("Division:", a / b);
elif choice == 5:
    print("Modulus:", a % b);
else:
    print('Invalid choice !!!')
