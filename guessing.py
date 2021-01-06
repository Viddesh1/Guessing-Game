while True:
    print("""
    ***** Welcome to the guessing Game *****
    Type 'Start' to Start the Game
    Type 'Stop' to Start the Game
    """)
    start_var = input("Enter 'Start' or 'Stop': ")
    if start_var == "Start" or start_var == "start":
        print("""  
        ***** Hints *****
        1) What is something that Allen Turing used to decode Nazi(Germans) Enigma Machine Code?
        2) It is something that protect our integrity over the Internet?
        3) C _ y t o _ _ _ P h y """)
        print()
        guess_name = input("Your Answer: ")
        if guess_name == "Crytography":
            print()
            print("**Congratulations the answer was Crytography**")
            break
        else:
            print()
            print("It was a Wrong Guess try again")
            
        
    elif start_var == "Stop" or start_var == "stop":
        break
    else:
        break
