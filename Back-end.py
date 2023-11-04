'''Will handle back-end for the project'''


fileText = open("generalQuestions.txt", "r")

text = fileText.readlines()


questions = []

for line in text:
    if line[1] == ")":
        if line[0] == "A":
            pass
        elif line[0] == "B":
            pass
        elif line[0] == "C":
            pass
        elif line[0] == "D":
            pass
        else:
            questions.append(line)
    else:
        questions.append(line)




