import random


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
      )


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


top_of_range = int(gamemode)
random_number = (random.randrange(0, top_of_range))
guesses = 0
last_guess = 'h'
hintenabled = False
guessed_values = []
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    #commands

    #quit command
    if user_guess == "quit":
        quit()

    #enable hints
    if user_guess == "enablehint":
        hintenabled = True
        print("Hints Enabled")
        continue

    if user_guess == "disablehint":
        hintenabled = False
        print("Hints Disabled")
        continue

    #hint command
    if user_guess == 'h' and hintenabled:
        if str(last_guess).isdigit():
            if int(last_guess) > random_number:
                print("Too high")
            elif int(last_guess) < random_number:
                print("Too low")
            continue
        elif last_guess == 'h':
            print("Please Guess One Time.")
            continue
        else:
            print("Please enter a valid syntax.")
        continue
    elif user_guess == 'h' and not hintenabled:
        print("Hints are not enabled")
        continue

    #history command
    if user_guess == 'hist':
        print("OLDEST -> NEWEST     ")
        print(guessed_values, sep=',')
        continue

    #Actual Check for Digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Wrong. Try Again.")
        last_guess = str(user_guess)
        guessed_values.append(int(user_guess))

print(f"You got it in {guesses} guesses.")
