'''Will handle back-end for the project'''


from flask import Flask, render_template

app = Flask(__name__)

fileText = open("generalQuestions.txt", "r") # change this so gets data from clicked and uses that file
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


@app.route('/') # currently set to home page, change to whatever page we name question and answer page
def default():
    return render_template("basic website html") # do I also need .html?

@app.route('/questions') # needs to coordinate with the HTML code
def index():
    return render_template('index.html', XXXXX=questions) # IMPORTANT replace XXXXX with the list in HTML

'''In the HTML section, need to make sure that /questions is set to the page name, /questions needs to interpret
the of question-class objects. HTML will have to get the question text, A, B, C, D (possibly using value = '{{ soandso}}'
format) and the answer from the objects to display them all, and hide the answer until an option is clicked'''