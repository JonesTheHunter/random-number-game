import random

#intro
print("Welcome to the number guessing game! Please choose your difficulty.\n"
      "1. Easy (10 numbers)\n"
      "2. Medium (100 numbers)\n"
      "3. Hard (1,000 numbers)\n"
      "4. Expert (1,000,000 numbers)\n"
      "5. Master (1,000,000,000 numbers)\n"
      "6. Nightmare (1,000,000,000,000 numbers)\n"
      "7. Custom\n"
      "\n"
      "Commands while in game:\n"
      "quit - quits the game\n"
      "h - gives hints (Off by Default)\n"
      "enablehint - enables hints\n"
      "disablehint - disables hints\n"
      "hist - shows previously guess numbers for oldest to newest\n"
      "enablehist - enable history (On by Default)\n"
      "disablehist - disable history (On by Default)\n"
      )

#pick game mode
gamemode = None
game_mode_picked = False
custom_game_mode = False
while not game_mode_picked:
    user_select = input("Pick Gamemode: ")
    if user_select == 'quit':
        quit()
    if user_select.isdigit():
        if user_select == '1':
            gamemode = int(11)
            break
        elif user_select == '2':
            gamemode = int(101)
            break
        elif user_select == '3':
            gamemode = int(1001)
            break
        elif user_select == '4':
            gamemode = int(1000001)
            break
        elif user_select == '5':
            gamemode = int(1000000001)
            break
        elif user_select == '6':
            gamemode = int(1000000000001)
            break
        elif user_select == '7':
            while not custom_game_mode:
                custom_select = input("Type a number: ")

                if custom_select.isdigit():
                    gamemode = int(custom_select)

                    if gamemode <= 0:
                        print('Please type a number larger than 0.')
                        continue
                    break
                else:
                    print('Please type a number.')
            break
        else:
            print("Please provide a number between 1-7.")
    else:
        print("Please provide a valid number.")

#Hint Mutations
print("Would you like to disable hint command? Y or N")

hintmutator = False
hintenabled = False
while True:
    mutation_confirm = input()

    if mutation_confirm.isalpha():
        if mutation_confirm.lower() == 'y':
            hintmutator = False
            hintenabled = True
        elif mutation_confirm.lower() == 'n':
            hintmutator = True
            hintenabled = False
        else:
            print("Please type y or n.")
            continue
    break

#Hist Mutations
histmutator = True
histenabled = True
print("Would you like to disable hist command? Y or N")
while True:
    mutation_confirm = input()

    if mutation_confirm.isalpha():
        if mutation_confirm.lower() == 'y':
            histmutator = False
            histenabled = True
        elif mutation_confirm.lower() == 'n':
            histmutator = True
            histenabled = True
        else:
            print("Please type y or n.")
            continue
    break

#main game
top_of_range = int(gamemode)
random_number = (random.randrange(0, top_of_range))
guesses = 0
last_guess = 'h'
guessed_values = []
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    #commands

    #quit command
    if user_guess == "quit":
        quit()

    # enable history
    if user_guess == "enablehist":
        if histenabled:
            print("hist already enabled.")
            continue
        else:
            histenabled = True
            continue

    #disable history
    if user_guess == "disablehist":
        if not histenabled:
            print("hist already disabled")
            continue
        else:
            print("hist command has been disabled.")
            histenabled = False
            continue

        #enable hints
    if user_guess == "enablehint":
        hintenabled = True
        print("Hints Enabled")
        continue

        #disable hints
    if user_guess == "disablehint":
        hintenabled = False
        print("Hints Disabled")
        continue

    #hint command
    if user_guess == 'h' and hintmutator:
        if hintenabled:
            if str(last_guess).isdigit():
                if int(last_guess) > random_number:
                    print("Too high")
                    continue
                elif int(last_guess) < random_number:
                    print("Too low")
                    continue
                elif last_guess == 'h':
                    print("Please Guess One Time.")
                    continue
                else:
                    print("Please enter a valid syntax.")
                continue
        else:
            print("Hints are not enabled. Type enablehint to enable.")
            continue
    elif not hintmutator and user_guess == 'h':
        print("hint command is disabled.")
        pass
    else:
        pass

    #history command
    if user_guess == "hist" and histmutator:
        if histenabled:
            if not guessed_values:
                print("No Values to print.")
                continue
            else:
                print("OLDEST -> NEWEST     ")
                print(guessed_values, sep=',')
                continue
        else:
            print("History is disabled. Type enablehist to enable.")
            continue
    elif not histmutator and user_guess == "hist":
        print("hist command is disabled.")
        pass
    else:
        pass

    #Actual Check for Digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess == "hist" or user_guess == "h" or user_guess == "enablehist" or user_guess == "disablehist" \
            or user_guess == "enablehint" or user_guess == "disablehint":
        continue
    else:
        print("Please type a valid number")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Wrong. Try Again.")
        last_guess = str(user_guess)
        guessed_values.append(int(user_guess))

print(f"You got it in {guesses} guesses.")
