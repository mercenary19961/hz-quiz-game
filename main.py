from question_bank import question_bank as q_bank

questions = q_bank

score = 0
question_number = 1

for q in questions:
    print(f"Question number:{question_number}\n")
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer is {q['answer']}.\n")

    question_number += 1
    print(f"Your current score is: {score}/{question_number - 1}\n")

print(f"Quiz finished! Your score: {score}/{len(questions)}")

