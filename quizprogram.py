from Question import Question

question_prompts = [
    "What is the capital of France?\nA) Paris\nB) Madrid\nC) Rome\n",
    "Who wrote 'To Kill a Mockingbird'?\nA) Ernest Hemingway\nB) Harper Lee\nC) J.K. Rowling\n",
    "What is the chemical symbol for water?\nA) H2O\nB) CO2\nC) NaCl\n"
]

questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "C"),
]





def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer: 
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + "Correct! ")


run_test(questions)