user = input("Enter a string: ")

if user:
    count = 0
    vowels = "aeiouAEIOU"
    
    for char in user:
        if char in vowels:
            count += 1
    
    print(f"Number of vowels: {count}")
else:
    print("Try again")