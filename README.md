# Password-Generator
Password Generator
Introduction
This Python script generates a random password based on user-defined criteria, including the lengths of lowercase letters, uppercase letters, numbers, and special characters. It utilizes a decorator to print a greeting message before and after generating the password.
Prerequisites
    • Python 3.x
How to Use
    1. Run the Script:
        ◦ Execute the script in a Python environment.
    2. Enter Criteria:
        ◦ The script will prompt you to enter the desired length for lowercase letters, uppercase letters, numbers, and special characters.
    3. Password Generation:
        ◦ The script will generate a random password based on the specified criteria.
    4. Output:
        ◦ The generated password will be displayed on the console.
        ◦ A thank you message will be printed after generating the password.
Code Structure
Libraries Used:
    • random: Generates random elements.
greet Decorator:
    • Description:
        ◦ Decorator function that prints a greeting message before and after executing the decorated function.
PasswordGenerator Class:
    • Constructor (__init__):
        ◦ Parameters:
            ▪ lowercase_len: Length of lowercase letters in the password.
            ▪ uppercase_len: Length of uppercase letters in the password.
            ▪ num_len: Length of decimal numbers in the password.
            ▪ spchar_len: Length of special characters in the password.
            ▪ pwd: List to store the generated password.
    • Function StoringWords():
        ◦ Generates random words for lowercase letters, uppercase letters, numbers, and special characters based on user-defined lengths. Randomly chosen characters are stored in the pwd list.
    • Function RandomPassword():
        ◦ Shuffles the pwd list to create a random password and prints it.
Example Usage:
    1. Input:
        ◦ Length of alphabets (Lower Case): 6
        ◦ Length of alphabets (Upper Case): 4
        ◦ Length of decimal number: 3
        ◦ Length of special characters: 2
    2. Output:
        ◦ Generated Password: aBcDeF123@$
        ◦ Message: Thanks for using this program :)

Note: This script provides a simple password generation functionality and can be further enhanced with additional features, such as allowing users to choose specific special characters or generating passwords in bulk.
