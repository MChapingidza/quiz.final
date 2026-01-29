questions = {
    "question_1": {
        "question":"what color is the sky?",
        "options": ["blue", "yellow", "red", "green", "purple"],
        "answer" : 1
    },
    "question_2": {
        "question":"what color is chocolate?",
        "options": ["blue", "yellow", "green", "purple", "brown"],
        "answer" : 5
    },
    "question_3": {
        "question": "what colour is paper?",
        "options": ["white", "yellow", "green", "brown", "purple"],
        "answer": 1
    },
    "question_4": {
        "question": "what color is mustard?",
        "options": ["white", "yellow", "green", "brown", "purple"],
        "answer" : 2
    },
    "question_5": {
        "question": "what color is blood?",
        "options": ["white", "yellow", "red", "brown", "purple"],
        "answer" : 3
    },

}
score = 0


def display_question(question_number):
    global score
    print(questions[question_number]["question"])

    for i, option in enumerate(questions[question_number]["options"], start=1):
        print(i, option)



    while True:
        try:
            guess = int(input("please enter an answer"))
            if 1 <= guess <= 5:
                if guess == questions[question_number]["answer"]:
                    score += 1
                break
            else:
                print("number must be between 1 and 5")
        except ValueError:
            print("please enter a number")


    return score

for key_q in questions:
    display_question(key_q)



print("well done you got", score, "out of", len(questions))