while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
       print("Invalid input. Please enter a valid number.")
limit = input("Enter the range: ")
limit = int(limit) if limit.isdigit() else 10
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")

print("End of the program")


    