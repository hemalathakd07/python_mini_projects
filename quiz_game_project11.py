print("***Welcome to my quiz game***")

question_bank=[
    {
        "text":"The ability of one class to acquire methods and attributes from another class is called ____",
        "answer":"A"
    },
    {
        "text":"Which of the following is a type of inheritance?",
        "answer":"D"
    },
    {
        "text":"What type of inheritance has multiple subclasses to a single superclass?",
        "answer":"C"
    },
    {
        "text":"What is the depth of multilevel inheritance in Python?",
        "answer":"C"
    },
    {
        "text":"What does MRO stand for?",
        "answer":"B"
    }
]

score=0 
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

options=[
        ["A. Inheritance","B. Abstraction","C. Polymorphism","D. Objects"],
        ["A. Single","B. Double","C. Multiple","D. both A and C"],
        ["A. Multiple Inheritance","B. Multilevel Inheritance","C. Hierarchical Inheritance","D. None of these"],
        ["A. Two level","B. Three level","C. Any level","D. None of these"],
        ["A. Method recurssive object","B. Method resolution order","C. Main resolution order","D. Method resolution object"]
]

for question_num in range(len(question_bank)):
    print("**************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    
    guess=input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("Correct answer")
        score+=1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {question_bank[question_num]["answer"]}")
    print(f"Your current score is {score}/{question_num+1}")

print(f"You have given {score} correct answers")
print(f"Your score is {(score/len(question_bank))*100}%")