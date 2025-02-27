print("Multiplication Table")

def generate_multiplication_table():
    number = int(input("Enter the number for the multiplication table: "))
    print(f"\nMultiplication Table for {number} (from 1 to 10):")
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1  
generate_multiplication_table()
print("Task is Done")

print("Task2")

num = int(input("Enter any Valid number: "))
r = int(input("Enter the Range: "))

for n in range(r):
    for nn in range(n+5):
        print(nn +1, end="")
    print("")  


for n in range(r):
    print("*" * (1+n))


for n in range(r):
  
    print(" " * (4 - n), end="")
    print("*" * (2 * n + 1))
print("THE END OF SCRIPT")