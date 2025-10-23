from quizbrain import QuizBrain

quizbrain = QuizBrain()

while range(10):
    score = 0
    question_number = 1

    while True:
        difficulty = input("Welcome to hz-quiz-game you will be asked 10 questions "
        "and you will choose these questions difficulties by typing e for easy, m for medium, h for hard: ").lower()
        
        if difficulty == 'e':
            q, a_option, a = quizbrain.easy_question_call()
            break
        elif difficulty == 'm':
            q, a_option, a = quizbrain.medium_question_call()
            break
        elif difficulty == 'h':
            q, a_option, a = quizbrain.hard_question_call()
            break
        else:
            print("wrong input please try again")
                
    print(f"Q{question_number}")
    print(q)
    print(a_option)
    choice = input("Choose between A/B/C/D: ").upper()
    if choice == a:
        print("Correct!\n")
        score += 1

    else:
        print(f"Wrong! The answer is {a}.\n")
    
    question_number += 1

print(f"Quiz finished! Your score: {score}/10")

# testing