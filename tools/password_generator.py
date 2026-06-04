import random
import string

lowercase = input("Do you want lowercase characters in your pass_list? (Y/n): ")
uppercase = input("Do you want uppercase characters in your pass_list? (Y/n): ")
digits = input("Do you want digits in your pass_list? (Y/n): ")
special = input("Do you want special characters in your pass_list? (Y/n): ")

length = int(input("Enter pass_list length: "))

if lowercase == 'Y':
    lowercase = True
else:
    lowercase = False
if uppercase == 'Y':
    uppercase = True
else:
    uppercase = False
if digits == 'Y':
    digits = True
else:
    digits = False
if special == 'Y':
    special = True
else:
    special = False

pass_list =''

if lowercase: pass_list += string.ascii_lowercase
if uppercase: pass_list += string.ascii_uppercase
if digits: pass_list += string.digits
if special: pass_list += string.punctuation

password = ''

for _ in range(length):
    password += random.choice(pass_list)

print("Your Password: ", password)