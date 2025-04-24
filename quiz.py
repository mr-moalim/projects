import random

print("Welcome to the General Knowledge Quiz!")
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote the play Romeo and Juliet?",
    "What is the largest ocean on Earth?",
    "What is the boiling point of water at sea level (in Celsius)?"
]
choices = [
    ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
    ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
    ["A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"]
]
answers = ["C", "B", "C", "D", "B"]

score = 0

for i in range(5):
    CQ = random.randint(0, len(questions) - 1)
    print(f"\nQuestion {i+1}: {questions[CQ]}")
    
    for choice in choices[CQ]: 
        print(choice)
    
    guess = input("Enter your answer (A/B/C/D): ").upper()

    if guess == answers[CQ]:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong ❌, the correct answer was {answers[CQ]}")
    
    questions.pop(CQ)
    choices.pop(CQ)
    answers.pop(CQ)

print(f"\nYou finished the test! Your final score is {score}/5 🎉")
