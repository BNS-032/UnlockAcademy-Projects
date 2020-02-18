#Ask For Info
user_name = input("Enter full name: ")
dob = input("Enter date of birth: ")
user_state = input("State: ")
user_country = input("Country: ")
user_is_active = input("Are you currently active in software developement? (Y/N): ").upper()
# Put Into Dictionary
user_dict = {"Name": user_name,
             "Date of birth": dob,
             "State": user_state,
             "Country": user_country,
             "Active Developer": user_is_active}

while True:
    try:
        # Ask user experience
        user_exp = input("How many years of experience do you have developing software?"
                         "\n [1] - Less than 1 year(s) of experience"
                         "\n [2] - 1-3 year(s) of experience"
                         "\n [3] - 3-8 year(s) of experience"
                         "\n [4] - 8+ year(s) of experience"
                         "\n Specify year(s) of experience: ")

        user_exp = int(user_exp)
        break
    except ValueError:
        print('\033[0;31m * OH NO! Missing input. Try again * \033[0m')

# Ask user to list known languages
coding_lang = input("How many languages do you know? (List and seperate them with commas)"
                            "\n For language"
                            "\n List Language(s): ")
coding_lang = coding_lang.split(",")

# Print Info
print(user_dict)
# Create if statement
if (user_exp) == 1:
    print('Average salary for level of experience is between $40,000-$60,000')
    if len(coding_lang) <= 3:
        print('Projected salary range for experience and knowledge of languages is between $40,000-$49,000.')
    else:
        if len(coding_lang) >= 3:
            print(
                ' Projected salary range for experience and knowledge of languages is between $50,000-$60,000.')
elif (user_exp) == 2:
    print('Average salary for level of experience is between $60,000-$80,000')
    if len(coding_lang) < 3:
        print('Projected salary range for experience and knowledge of languages is between $60,000-$69,000.')
    else:
        if len(coding_lang) >= 3:
            print(
                'Projected salary range for experience and knowledge of languages is between $70,000-$80,000.')
elif (user_exp) == 3:
    print('Average salary for level of experience is between $80,000-$120,000')
    if len(coding_lang) < 3:
        print('Projected salary range for experience and knowledge of languages is between $80,000-$99,000.')
    else:
        if len(coding_lang) >= 4:
            print(
                'Projected salary range for experience and knowledge of languages is between $100,000-$120,000.')
elif (user_exp) == 4:
    print('Average salary for level of experience is at least $130,000')
    if len(coding_lang) <= 3:
        print('Projected salary: $' + str(130000 + (2500*(len(coding_lang)))))
    else:
        if len(coding_lang) >= 4:
            print('Projected salary: $' + str(130000 + (3500*(len(coding_lang)))))
else:
    print('Invalid input')
