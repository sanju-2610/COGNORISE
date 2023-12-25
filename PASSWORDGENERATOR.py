import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!@$%^&*(')"

while 1:
    password_len = int(input("Enter the length of the password : "))
    password_count = int(input("Number of passwords : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Your password : ", password)    
                    