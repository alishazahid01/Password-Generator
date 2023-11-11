#Password Generator
#importing random library to generate random code 
import random

#Creating a decorator
def greet(func):
    def mfx(*args, **kwargs):
        print("Password Generated")
        func(*args, **kwargs)
        print("Thanks for using this program :)")

    return mfx

#creating password generator class
class PasswordGenerator():
    
    #creating constructor
    def __init__ (self, lowercase_len:int, uppercase_len:int, num_len:int, spchar_len:int,pwd):
        self.lowercase_len = lowercase_len
        self.uppercase_len = uppercase_len
        self.num_len = num_len
        self.spchar_len = spchar_len
        self.pwd = pwd
    
    # creating function to generating random words
    def StoringWords(self):
        num_list = [1,2,3,4,5,6,7,8,9]
        lowercase_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        uppercase_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        special_char = ['@',"#","$","*","?"]


        #Loop to generate random words from the alphabets_list
        for i in range (lowercase_len):
            gen_word = random.choice(lowercase_list)
            # append genrated word into the list
            pwd.append(gen_word)

         #Loop to generate random words from the alpha_list2
        for i in range (uppercase_len):
            gen_word = random.choice(uppercase_list)
            # append genrated word into the list
            pwd.append(gen_word)

         #Loop to generate random words from the num_list
        for i in range (num_len):
            gen_word = random.choice(num_list)
            # append genrated word into the list
            pwd.append(gen_word)

         #Loop to generate random words from the special_char
        for i in range (spchar_len):
            gen_word = random.choice(special_char)
            # append genrated word into the list
            pwd.append(gen_word)
        
       
    # creating a function to generate random passwords from the random choosed words
    @greet
    def RandomPassword(self):

        #Shuffle list
        random.shuffle(pwd)
        
        generated_pass = ''.join(str(item) for item in pwd)
        print(generated_pass)

# Taking length of the password     
lowercase_len = int(input("Length of alphabets(Lower Case) : "))
uppercase_len = int(input("Length of alphabets(Upper Case) : "))
num_len = int(input("Length of decimal number : "))
spchar_len = int(input("Length of the special character : "))

 #creating empty list to append random generated words
pwd = []

#Calling PasswordGenerator class
input_object = PasswordGenerator(lowercase_len,uppercase_len,num_len,spchar_len,pwd)

#Calling GeneratingPassword Function 
input_object.StoringWords()

#Calling RandomPassword Function
input_object.RandomPassword()