import random
import array
print ("Hello,Welcome to password genarator!")
MAX_LEN = 12
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
Lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']  
Upercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']
COMBINED_LIST = Digits + Upercase_letters + Lowercase_letters + Symbols
rand_digit = random.choice(Digits)
rand_upper = random.choice(Upercase_letters)
rand_lower = random.choice(Lowercase_letters)
rand_symbol = random.choice(Symbols)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
    password = ""
for x in temp_pass_list:
        password = password + x
print("Your Password is:")
print(password)
