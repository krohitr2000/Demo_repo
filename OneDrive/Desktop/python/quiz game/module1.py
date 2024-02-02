#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     14-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print("******************************")
print("**** Welcome to quiz ****")
questions=[
{"text" : "What happens when '2' == 2 is executed?", "Answer" :"A"},
{"text" : "Which one of the following is the correct extension of the Python file?", "Answer" :"A"},
{"text" : "Which character is used in Python to make a single line comment?", "Answer" :"C"},
{"text" : " Which of the following statements is correct regarding the object-oriented programming concept in Python?",
"Answer" : "B"}
]

answers=[
["A : False", "B : Ture", "C : ValueError occurs", "D : TypeError occurs"],
['A : .py', "B : .python", "C : .p", "D : None of these"],
['A : /', "B : //", "C : #", "D : !"],
['A : Classes are real-world entities while objects are not real', "B :Objects are real-world entities while classes are not real",
 "C :Both objects and classes are real-world entities", "D :All of the above"]
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

for que in range(len(questions)):
    print("**********************")
    print((questions)[que]["text"],"\n")
    for i in (answers[que]):
        print(i)


    guess=input('\nEnter your answer (A/B/C/D) :').upper()
    is_correct=check_answer(guess,questions[que]['Answer'])

    if is_correct:
        score+=1
        print('Correct answer')
        print(f'Score : {score}/{que+1}')
    else:
        print('Incorrect answer\n')
        print(f"The correct answer is {questions[que]['Answer']}")
        print(f'\n Score : {score}/{que+1}')
print(f'\n Your final score is : {score}')
print(f" Your score is : {'(score/len(questions)*100'}")