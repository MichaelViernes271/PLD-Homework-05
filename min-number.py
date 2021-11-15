"""
Topic: Programming Logic and Desin
Author: Viernes, Michael
College: BSCOE 1-1
Submitted to: Mr. Danilo Madrigalejos
"""

# =================NOTE===================
# PLEASE TRY SEARCHING FOR SWITCH 
# STATEMENT IN PYTHON IF ANY.
# ALSO, RESEARCH ABOUT DECOR FUNCS


                                        # ################### #
                                        #  Efficient sorting  #
                                        # ################### #




def minNum(numlist): # Find the min number among the inputs.
    # print(str(numlist[0]))
    return numlist[0]

def sortNum(numlist): # Sorts two numbers.
    # print("sortNum()" + str(numlist))
    # print("sorting " + str(numlist.sort()))
    sorted_list = list(numlist)
    sorted_list.sort()
    # print("the sorted list" + str(sorted_list))
    return sorted_list
    
def askNum(): # Asks a multiple numbers.
    numlist = []
    for i in range(1, 4):
        # print(i)
        numlist.append((int(input("Type an integer: "))))
    # print("the list" + str(numlist))
    return numlist.copy()
def main(): # main().
    u_numlist = []
    u_numlist = list(askNum())
    # print(f"askNum() has finished its task!\n {u_numlist}")
    u_numlist = sortNum(list(u_numlist))
    # print(f"sortNum() has finished its task!\n{u_numlist}")
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