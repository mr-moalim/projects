print("Welcome to Wordle!")
print("Write 'QUIT' to exit")
Answer = ["A", "H", "M", "E", "D"]  # Using list for consistency
tries = 0

def get_guess():
    while True:
        guess = input("Guess a 5-letter word: ").upper()
        if guess == "QUIT":
            print("Goodbye!")
            exit()
        elif len(guess) != 5:
            print("Please enter exactly 5 letters!")
        else:
            return list(guess)

def check(guess, answer):
    used = [False] * len(answer)
    correctletter = []
    wrongletter = []
    incorrect = 0  # Initialize incorrect counter

    # First pass: Check correct positions
    for i in range(len(answer)):
        if guess[i] == answer[i]:
            used[i] = True
            correctletter.append(guess[i])

    # Second pass: Check wrong positions
    for i in range(len(answer)):
        if guess[i] != answer[i]:
            found = False
            for j in range(len(answer)):
                if not used[j] and guess[i] == answer[j]:
                    used[j] = True
                    found = True
                    wrongletter.append(guess[i])
                    break
            if not found:
                incorrect += 1  # Increment incorrect count

    print(f"Correct letters in position: {correctletter}")
    print(f"Letters in word but wrong position: {wrongletter}")
    
    return len(correctletter) == len(answer)  # Check if the whole word is guessed

# Game loop
while tries < 6:
    print(f"\nAttempt {tries + 1}/6")
    guess = get_guess()
    
    if check(guess, Answer):
        print("Congratulations! You guessed the word!")
        break
    
    print("--------------------------")
    tries += 1
else:
    print(f"Game over! The word was: {''.join(Answer)}")