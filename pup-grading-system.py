"""
Topic: Programming Logic and Desin
Author: Viernes, Michael
College: BSCOE 1-1
Submitted to: Mr. Danilo Madrigalejos
"""


while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break