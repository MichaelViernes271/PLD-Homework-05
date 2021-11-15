"""
Topic: Programming Logic and Desin
Author: Viernes, Michael
College: BSCOE 1-1
Submitted to: Mr. Danilo Madrigalejos
"""

# =================NOTE===================
# X = PLEASE TRY SEARCHING FOR SWITCH 
# X = STATEMENT IN PYTHON IF ANY.
# X = ALSO, RESEARCH ABOUT DECOR FUNCS.
# ========================================

def askAge(): # Requests age.
    age = None
    
    try:
        age = int(input("What is your age: "))
        if age == None or age == "":
            raise TypeError
    except TypeError as e:
        print(f"Your input was \"{age}\" which raises exception: {str(e)}")
    
    return age

def compareAge(u_age): # Returns the age class.

    kid, teen, debut, adult = 12, 19, 17, 18
    
    try:
        
        if u_age <= kid:
            return "kid"
        elif kid < u_age <= teen:
            return "teen"
        elif debut == u_age:
            return "debut"
        elif u_name > adult:
            return "adult"
        else:
            return "Not a valid value. Please try again."
    except InvalidInput:
        print(InvalidInput)



def printAge(age, category): # Prints result.
    print_age_result = """
    The age entered {} is classified as \"{}\"
    """
    print(print_age_result.format(age, category))
    pass
    
def main(): # Main().
    print(
    """
       \n\n
========================================
\t\tLIFE STAGES
=======================================
Instructions: Enter an age to print\n \rits classification.\n
    """)
    age = askAge()
    ageCateg = compareAge(age)
    printAge(age, ageCateg)
    
while True:
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
    if quit == 'y' or quit != 0 or quit == None or quit == "":
        break
        