with open("pifile.txt") as file_object:
    lines = file_object.readlines()
    pi_strings = ''

    for line in lines:
        pi_strings+=line.strip()

birthday = input("Enter your bday in ddmmyy format :")
if birthday in pi_strings:
    print("Your bday is found in first million digits of pi")
else:
    print("Your bday does not appear in first million digits of pi")