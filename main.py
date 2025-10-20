questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 12", "C) 13", "D) 11"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer is {q['answer']}.\n")

print(f"Quiz finished! ya bro Your score: {score}/{len(questions)}")

# this is from zaid