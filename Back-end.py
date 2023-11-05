'''Will handle back-end for the project'''


import json

fileText = open("generalQuestions.txt", "r")
answerText = open("generalAnswers.txt", "r")

text = fileText.readlines()

answerfile = answerText.readlines()

questions = []



class question:
    def __init__(self, questionText, A, B, C, D, answer):
        self.questionText = questionText
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.answer = answer


answers = []

for line in answerfile:
    answers.append(line[0]) # just using the letter to verify answer
    

for line in text:
    if line in ("", " ", "\n"):
        text.remove(line)



previousLineWasQuestion = False
for line in text:
        
    if line[1] == ")":
        if line[0] == "A":
            A = line
            print(A)
            
        elif line[0] == "B":
            B = line
            
        elif line[0] == "C":
            C = line
            
        elif line[0] == "D":
            D = line
            if questions == []:
                questions.append(question(questionText, A, B, C, D, answers[len(questions)]))
        else:
            questionText = line
            print("Hit text")
            if questions != []: #as long as it isn't the first question, we should immediately append the last data
                questions.append(question(questionText, A, B, C, D, answers[len(questions)]))
                print("index = ", len(questions))

    else:
        questionText = line
        print("index = ", len(questions))
        if questions != []: #as long as it isn't the first question, we should immediately append the last data
            questions.append(question(questionText, A, B, C, D, answers[len(questions)]))





questions.append(question(questionText, A, B, C, D, answers[-1])) # because the appending is triggered when the next question is asked


