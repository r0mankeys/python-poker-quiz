print("Welcome to my Poker Quiz!")

quiz_answers = {
    "question_1": "Texas Hold'em",
    "question_2": "Pocket Aces",
    "question_3": "Two",
    "question_4": "Royal Flush",
    "question_5": "Fold",
    "question_6": "Hole Cards",
    "question_7": "Burn",
} 

quiz_score = 0

wishes_to_play = input("Do you want to play? (yes/no) ")

if wishes_to_play == "yes":
    print("Great! Let's get started.")
else:
    print("That's too bad. Maybe next time.")

question_1 = input("Question 1: What is the most popular form of poker? ")

if question_1 == quiz_answers["question_1"].lower() or question_1 == quiz_answers["question_1"]:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Texas Hold'em.")

question_2 = input("Question 2: What is the best starting hand in poker? ")

if question_2 == quiz_answers["question_2"].lower() or question_2 == quiz_answers["question_2"]:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Pocket Aces.")

question_3 = input("Question 3: How many hole cards do players receive in Texas Hold'em? ")

if question_3 == quiz_answers["question_3"].lower() or question_3 == quiz_answers["question_3"] or int(question_3) == 2:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Two.")

question_4 = input("Question 4: What is the best possible hand in poker? ")

if question_4 == quiz_answers["question_4"].lower() or question_4 == quiz_answers["question_4"]:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is a Royal Flush.")

question_5 = input("Question 5: What is it called when a player decides not to play a hand? ")

if question_5 == quiz_answers["question_5"].lower() or question_5 == quiz_answers["question_5"]:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Fold.")

question_6 = input("Question 6: What is another term for a player's starting hand? ")

if question_6 == quiz_answers["question_6"].lower() or question_6 == quiz_answers["question_6"]:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Hole Cards.")

final_question = input("Question 7: What is it called when a card is removed from the deck before dealing? ")

if final_question == quiz_answers["question_7"].lower() or final_question == quiz_answers["question_7"]:
    quiz_score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Burn.")

if quiz_score == 7:
    print("Congratulations! You got a perfect score!")
elif quiz_score >= 4:
    print(f"Good job! You got {quiz_score} out of 7 questions correct.")
else:
    print(f"Oof looks like somemone needs to brush up on their poker knowledge. You got {quiz_score} out of 7 questions correct.")

print("\nThanks for playing!")
