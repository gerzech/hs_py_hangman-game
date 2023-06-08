import random
def hangman_game():
    words_db = ["python", "java", "swift", "javascript"]
    var_won = 0
    var_lost = 0
    while True:
        print(f'H A N G M A N\nType "play" to play the game, "results" to show the scoreboard, ' \
                                                                     'and "exit" to quit:')
        user_input = input()
        if user_input == "exit":
            return None
        if user_input == "results":
            print(f"You won: {var_won} times.\nYou lost: {var_lost} times.")
            continue
        if user_input != "play":
            continue
        solution = random.choice(words_db)
        output = "-" * len(solution)
        attempts = 8
        guesses = ""
        while attempts > 0:
            print(f"\n{output}\nInput a letter:")
            letter = input()
            if len(letter) != 1:
                print("Please, input a single letter.")
                continue
            if not letter.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if letter in guesses:
                print("You've already guessed this letter.")
                continue
            guesses += letter
            if letter not in solution:
                attempts -= 1
                print("That letter doesn't appear in the word.")
                continue
            else:
                count = solution.count(letter)
                position = solution.find(letter)
                while count > 0:
                    if count < solution.count(letter):
                        position = solution.find(letter, position + 1)
                    if position == 0:
                        output = letter + output[1:]
                    elif position == (len(solution) - 1):
                        output = output[:position] + letter
                    else:
                        output = output[:position] + letter + output[position + 1:]
                    count -= 1
            if output == solution:
                print(f"\n{output}\nYou guessed the word {solution}!\nYou survived!")
                var_won += 1
                break
        if output != solution:
            print("You lost!")
            var_lost += 1


hangman_game()