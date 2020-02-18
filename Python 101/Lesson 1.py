# Ask user experience
user_exp = input("How many years of experience do you have developing software?"
                 "\n [1] - Less than 1 year(s) of experience"
                 "\n [2] - 1-3 year(s) of experience"
                 "\n [3] - 3-8 year(s) of experience"
                 "\n [4] - 8+ year(s) of experience"
                 "\n Specify year(s) of experience: ")

# Create if statement
user_exp = int(user_exp)
if (user_exp) == 1:
    print('Average salary for level of experience is between $40,000-$60,000')
elif (user_exp) == 2:
    print('Average salary for level of experience is between $60,000-$80,000')
elif (user_exp) == 3:
    print('Average salary for level of experience is between $80,000-$120,000')
elif (user_exp) == 4:
    print('Average salary for level of experience is at least $130,000')
else: print('Invalid input')
