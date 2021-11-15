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
    except ValueError as e:
        print(
        f"""
        !!!!!!!WARNING!!!!!!!!!!!!!!!!!!!!WARNING!!!!!!!!!!!!!!!!!!
        NING!!!!!!!!!!!!!!!!!!!!!!WARNING!!!!!!!!!!!!!!!!!!!!!!!WAR
        
        Your input was \"{age}\" which raises \n\texception: {str(e)}\n
    
        !!!!!!!WARNING!!!!!!!!!!!!!!!!!!!!WARNING!!!!!!!!!!!!!!!!!!
        NING!!!!!!!!!!!!!!!!!!!!!!WARNING!!!!!!!!!!!!!!!!!!!!!!!WAR
        """
        )
    
    return age

def compareAge(u_age): # Returns the age class.

    kid, teen, debut, adult = 12, 19, 17, 18
    
    if u_age <= kid:
        return "kid"
    elif kid < u_age <= teen:
        return "teen"
    elif debut == u_age:
        return "debut"
    elif u_age >= adult:
        return "adult"
    else:
        print("Cannot identify. Please redo.")
        raise Exception

def printAge(age, category): # Prints result.
    print_age_result = """
    The age entered {} is classified as \"{}\".
    """
    print(print_age_result.format(age, category))
    pass
    
def main(): # Main().
    print(
    """
       \n\n
========================================
\t\tLIFE STAGES\n
    0 - 12: Kid     13 - 17: Teen
    18: Debut       19 and above: Adult

========================================

Instructions: Enter an age to print\n \rits classification.
    """)
    age = askAge()
    ageCateg = compareAge(age)
    printAge(age, ageCateg)
    
while True:
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break
    