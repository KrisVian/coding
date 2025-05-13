import random

COLOURS = ["R", "B", "O", "Y", "G", "WR"]
TRIES = 10
CODE_LENGTH = 3

def generate_code():
    code = []


    for _ in range(CODE_LENGTH):
        colour = random.choice(COLOURS)
        code.append(colour)

    return code

def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colours.")
            continue

        for colour in guess:
            if colour not in COLOURS:
                print(f"Invalid colour: {colour}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    colour_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for colour in real_code:
        if colour not in colour_counts:
            colour_counts[colour] = 0
        colour_counts[colour] += 1

    for guess_colour, real_colour in zip(guess, real_code):
        if guess_colour == real_colour:
            correct_pos += 1
            colour_counts[guess_colour] -= 1

    
    for guess_colour, real_colour in zip(guess, real_code):
        if guess_colour in colour_counts and colour_counts[guess_colour] > 0:
            incorrect_pos += 1
            colour_counts[guess_colour] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code.")
    print("The valid colours are", *COLOURS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries.")
            break
        
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    
    else:
        print("You ran out of tries, the code was:", *code)



if __name__ == "__main__":
    game()