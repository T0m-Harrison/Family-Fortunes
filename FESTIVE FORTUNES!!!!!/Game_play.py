import pandas as pd
from random import randint
#This section allows teams to name themselves and should be executed at the start of the game

print('''WELCOME TO FESTIVE FORTUNES!!!!!!!!!!!!
To begin, name each of the 2 teams,
Then type 'START' to begin!!!!!!!!!''')
team1 = input("What do you want the first team to be called? ")
team2 = input("What do you want the second team to be called? ")
hold = 0
points1 = 0
points2 = 0
toask = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
questions = pd.read_csv('Questions.csv')

print("Team", team1, "call 1 or 2!")
callanswer = int(input())
flip = randint(1, 2)
if callanswer == flip:
    hold = team1
else:
    hold = team2
print(hold, "YOUR QUESTION!!!")
asking = randint(1, len(toask))
asking = asking - 1
question = questions.loc[asking, 'Questions']
answers = questions.T
answers = answers[asking].tolist()
toask.pop(asking)
print(toask)
print(question)
answers.pop(0)
points = 0
print(hold, "what is your answer?")
guess = input()
guess1 = 0
guess2 = 0	
correct = 0
for i in range ( len(answers)):
    if answers[i].lower() == guess.lower():
        if hold == team1:
            r = i + 1
            guess1 = r * 10
            print(hold, "that's", guess1, "points!")
        elif hold == team2:
            r = i + 1
            guess2 = r * 10
            print(hold, "that's", guess2, "points!")
        print("DING DING DING!!!", guess, "is place number", len(answers) - i)
        correct = 1
        r = 0
        while r < len(answers):
            if answers[r].lower() == guess.lower():
                answers[r] = "Guessed"
            r += 1
if correct == 0:
    print("WRONG")
    if hold == team1:
        guess1 = 0
    elif hold == team2:
        guess2 = 0
if hold == team1:
    hold = team2
else:
    hold = team1
print(hold, "your turn to answer")
print("As a reminder, the question is", question)
guess = input("What is your answer? ")
correct = 0
for i in range (len(answers)):
    if answers[i].lower() == guess.lower():
        if hold == team1:
            r = i + 1
            guess1 = r * 10
            print(hold, "that's", guess1, "points!")
        elif hold == team2:
            r = i + 1
            guess2 = r * 10
            print(hold, "that's", guess2, "points!")
        print("DING DING DING!!!", guess, "is place number", len(answers) - i)
        correct = 1
        r = 0
        while r < len(answers):
            if answers[r].lower() == guess.lower():
                answers[r] = "Guessed"
            r += 1
if correct == 0:
    if hold == team1:
        guess1 = 0
    elif hold == team2:
        guess2 = 0
if guess1 > guess2:
    hold = team1
elif guess2 > guess1:
    hold = team2
elif guess1 == guess2:
    print("Team", team1, "call 1 or 2!")
    callanswer = int(input())
    flip = randint(1, 2)
    if callanswer == flip:
        hold = team1
        points1 = guess1 + guess2
    else:
        hold = team2
        points2 = guess1 + guess2

def basegame():
    global team1
    global team2
    global hold
    global toask
    global questions
    global points1
    global points2
    print(hold, "YOUR QUESTION!!!")
    asking = randint(1, len(toask))
    asking = asking - 1
    question = questions.loc[asking, 'Questions']
    answers = questions.T
    answers = answers[asking].tolist()
    toask.pop(asking)
    print(question)
    print(toask)
    answers.pop(0)
    count = 0
    points = 0
    while count < len(answers):
        guess = input("What is your guess? ")
        steal = 1
        for i in range(len(answers)):
            currentanswer = answers[i]
            if currentanswer.lower() == guess.lower():
                count += 1
                steal = 0
                print("DING DING DING!!!", guess, "is place number", 5 - i)
                r = 0
                while r < len(answers):
                    if answers[r] == guess:
                        answers[r] = "Guessed"
                    r += 1
                r = i + 1
                points += r * 10
        if steal == 1:
            print("UH OH, that was WRONG!", hold, "you lose hold of the questions")
            if hold == team1:
                hold = team2
            else:
                hold = team1
    if hold == team1:
        points1 += points
        print(team1, "that's", points, "points this round")
        print("Your total is now", points1)
    else:
        points2 += points
        print(team2, "that's", points, "points this round")
        print("Your total is now", points2)


for i in range (5):
    basegame()