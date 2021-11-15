"""
Topic: Programming Logic and Desin
Author: Viernes, Michael
College: BSCOE 1-1
Submitted to: Mr. Danilo Madrigalejos
"""

# =================REMINDER NOTE===================
# PLEASE TRY SEARCHING FOR SWITCH 
# STATEMENT IN PYTHON IF ANY.
# ALSO, RESEARCH ABOUT DECOR FUNCS.

def minNum(numlist): # Find the min number among the inputs.
    return numlist[0]

def sortNum(numlist): # Sorts two numbers.
    sorted_list = list(numlist)
    sorted_list.sort()
    return sorted_list
    
def askNum(): # Asks a multiple numbers.
    numlist = []
    for i in range(1, 4):
        numlist.append((int(input("Type an integer: "))))
    return numlist.copy()
def main(): # main().
    u_numlist = []
    u_numlist = list(askNum())
    u_numlist = sortNum(list(u_numlist))
    min_num = minNum(u_numlist)
    print(f"The minimum value among {list(u_numlist)} is {min_num}.\n")
    
while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
    if (quit == 'y' or quit == 0):
        print("Closing...")    
        break