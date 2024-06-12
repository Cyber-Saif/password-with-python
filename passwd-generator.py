#passwd-generator                 
#January 13, 2022

import string
import random

#list of 0-9 digits 
digt = list(string.digits)

#letters in lower case as a list
lwr_case = list(string.ascii_lowercase)

#uppercase list
upper_case = list(string.ascii_uppercase)

#special characters list
punc = list(string.punctuation)


#function will require parameters, for example how many digits you want in your password, the total length of your password
def password_generator(total, capital, punctuations, digits):
    total, capital, punctuations, digits = int(total), int(capital), int(punctuations), int(digits)
    passwd = []
    count = capital + punctuations + digits
    
    #checking that generated password is in the range of total 
    if count>total:
        print(f'\nYour have given {total} characters for total \nbut you choose {count},next time make sure to increase your total character`s range')

    calc = 0

    if count == 0:
        calc = total
    else:
        calc = total - count
        
    
    if total:
        #generating capital letter as user wants
        for capital in range(capital):
            passwd.append(random.choice(upper_case))
        #digits 
        for digit in range(digits):
            passwd.append(random.choice(digt))
        #punctuations
        for punctuation in range(punctuations):
            passwd.append(random.choice(punc))
        #if there is an extra space like user wants 9 total(3 capital, 3 digits, 2 punc) so here
        #program automatically generate 2 letters of lowers_case to complete total range
        for total in range(calc):
            passwd.append(random.choice(lwr_case))

    if len(passwd)<8:
        print("\n!!your total characters are less than 8! pls selec more than 7 press f5 to generate a new one ")

    random.shuffle(passwd)
    return "".join(passwd)
    

# main function which will call the generator and set the arguments to the function call
def main():

    print("please select at least 8 characters")

    total = input('\ntype total characters you want: ')
    
    #the while loop with an empty string is to check if user has specified something or not
    #if not then it will keep asking for total
    while total == "":
        print("Total characters are 0 program will not go further, try again")
        total = input('\ntype total characters you want: ')
    
    #while with isdigits are to check if the input int or not if not it will ask again
    while not total.isdigit():
        print("intigers expected")
        total = input('\ntype total characters you want: ')

    #Finally when we have a valid total number we will check if the choosen number is lees than 8
    while int(total)<8:
        print("your password is little short,to generate a secure one type 8 or more")
        total = input('\ntype total characters you want: ')

    if total == "done":
        print(">>exiting the program")
        exit()


    #we will ask user to enter at least one capital, samll, digit and special character
    #total capital letters user want
    capital = input('\nnumber of capital letters you want: ')   
    while capital == "":
        print("You must have one Capital letter")
        capital = input('\nnumber of capital letters you want: ')   
    
    if capital == "done":
        print(">>exiting the program")
        exit()
    
    while not capital.isdigit():
        print("intigers expected")
        capital = input('\nnumber of capital letters you want: ')   


    pnc = input('\nnumber of punctuations you want: ')
    while pnc == "":
        print("You must have one punctuation")
        pnc = input('\nnumber of punctuations you want: ')
        
    
    if pnc == "done":
        print(">>exiting the program")
        exit()

    while not pnc.isdigit():
        print("intigers expected")
        pnc = input('\nnumber of punctuations you want: ')     


    nmbr = input('\ntype total digits you want: ')
    while nmbr == "":
        print("You must have one digit")
        nmbr = input('\ntype total digits you want: ')
    
    if nmbr == "done":
        print(">>exiting the program")
        exit()

    while not nmbr.isdigit():
        print("intigers expected")
        nmbr = input('\ntype total digits you want: ')

    pwd = password_generator(total, capital, pnc, nmbr)
    print(f'Generated Pssword Is {pwd}')
     
    return pwd

main()           
        
