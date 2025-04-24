import random
import json
print("Welcome to the Flashcards!")
question_file="C:/Users/Yousef/Desktop/python/Ahmed/flashcards/flashcards.json"

class Flasher:
    def __init__(self,question,options,answer):
        self.question= question
        self.options= options
        self.answer= answer


    def add_flashcard(self):
        question = input("Enter your question: ")
        options = []
        for i in range(4):
            options.append(input(f"Enter option {i+1}: "))
        answer = input("Enter the letter of the correct answer (A/B/C/D)): ").upper()
        flashcards.append({"question": question, "options": options, "answer": answer})
        save()


    def delete(self):
        for card in flashcards:
            print(card["question"])
        try:
            remove_question = int(input("Type the number of the question you want to delete: "))
            if 0 < remove_question < len(flashcards)+1:
                remove_question -= 1
                flashcards.pop(remove_question)
                save()
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

    def quiz(self):
        random.shuffle(flashcards)  
        score = 0  

        for j in range(len(flashcards)):
            print("--------------------------------------")  
            print(f"Question {j+1}: {flashcards[j]['question']}")  
            print(flashcards[j]['options'])  

            ans = input("Enter your answer(A/B/C/D): ").upper()
            if ans == flashcards[j]['answer']:  
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {flashcards[j]['answer']}")
            print("--------------------------------------")
            print()

        print(f"You finished the quiz! Your score is {score}/{len(flashcards)}")

def save():
    with open(question_file,"w") as file:
        json.dump((flashcards),file,indent=4)

try:
    with open(question_file, "r") as file:
        content = file.read().strip()
        if content:
            flashcards = json.loads(content)
        else:
            flashcards = []
except (FileNotFoundError, json.JSONDecodeError):
    flashcards = []


play = True
while play:
    try:
        T = int(input("Do you want to (1. Play / 2. Add question / 3. Remove question / 4. Quit): "))
        if T == 1:
            Flasher.quiz(flashcards)
            print()
        elif T == 2:
            Flasher.add_flashcard(flashcards)
            print()
        elif T == 3:
            Flasher.delete(flashcards)
            print()
        elif T == 4:
            play = False
        else:
            print("Choose a number between 1-4")
    except ValueError:
        print("Choose a number between 1-4")
        continue

print("Goodbye!")
