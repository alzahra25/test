def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

while True:
    user_input = input("Enter a string: ").strip()
    if user_input:
        vowel_count = count_vowels(user_input)
        print(f"The number of vowels in '{user_input}' is {vowel_count}")
        break
    else:
        print("Input cannot be empty. Please enter a valid string.")