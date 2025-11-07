from questions import questions


def welcome():
    print("------------------------------------------------------")
    print("            WELCOME TO  THE PYTHON QUIZ              ")
    print("------------------------------------------------------")
    print("Answer each question by typing A, B, C, or D.\n")
    print("Let's test your Python knowledge!\n")


def ask_question(question, options, correct_option):
    print(question)
    for option in options:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == correct_option:
        print(" Correct!\n")
        return True
    else:
        print(f" Wrong! Correct answer is {correct_option}\n")
        return False


def run_quiz():
    welcome()
    score = 0

    # list of 30 Python questions in other file and impor this file becouse of space
    
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print("===================================")
    print(f" Quiz Completed! Your Score: {score}/{len(questions)}")
    print("===================================")

    if score == len(questions):
        print(" Excellent! You're a Python Master!")
    elif score >= 20:
        print(" Great Job! Keep it up.")
    elif score >= 10:
        print(" Good attempt! Practice more.")
    else:
        print(" Keep learning! Review W3Schools again.")
        
        
run_quiz()        


