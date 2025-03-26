'''2. Guess the Number Game:

    Create a function that generates a random number 
    within a range specified by the user.
    Prompt the user to guess the number within a specified 
    maximum number of attempts.
    Provide feedback to the user after each guess, indicating 
    whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number 
    correctly or reaches the maximum number of attempts.
'''

def generate_random(from_, to):
    n: int = 0
    for i in range(to-from_+1):
        n += to * 7.3 * i
    numero = int((n % (to-from_+1) + from_) // 1)
    return numero

print(generate_random(1,3))

guesses: int = 5
already_guessed: int = 0
while already_guessed < guesses:
    guess = input(f"Inserisci un numero, {guesses-already_guessed} tentativi rimanenti: ")
    if guess.is_integer() == True:


