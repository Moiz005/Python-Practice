#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
i = 0
j = 0
num_letters = 0
num_symbols = 0
num_numbers = 0
lengthOfPassword = nr_letters + nr_symbols + nr_numbers
for i in range(lengthOfPassword):
    choice = random.randint(0, 2)
    if choice == 0 and  num_letters < nr_letters:
        num = random.randint(0, len(letters) - 1)
        password += letters[num]
        num_letters += 1
    elif choice == 1 and num_symbols < nr_symbols:
        num = random.randint(0, len(symbols) - 1)
        password += symbols[num]
        num_symbols += 1
    elif choice == 2 and num_numbers < nr_numbers:
        num = random.randint(0, len(numbers) - 1)
        password += numbers[num]
        num_numbers += 1
print(password)
