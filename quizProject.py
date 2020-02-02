# QUIZ PROGRAM TEST ON ENGLISH LANGUAGE
def my_question(quest, Tscore):
    print(quest + '\n')
    fulName = input("Enter your Full Name to Get Started: ")
    print ('Hello', fulName,'!' '\n' 'Welcome to English Online Quiz Class!')
    answer1 = input("Attempt Question 1: ")
    answer2 = input("Attempt Question 2: ")
    answer3 = input("Attempt Question 3: ")
    answer4 = input("Attempt Question 4: ")
    print ('Find below your performance:')
    if answer1 == "c":
        print('question-1', answer1,'is correct', + Tscore, 'marks')
    else:
        print('question-1', answer1, 'is not correct', + Tscore-Tscore, 'mark' )
    if answer2 == "b":
        print('question-2', answer2, 'is correct', + Tscore, 'marks')
    else:
        print('question-2', answer2, 'is not correct', + Tscore-Tscore, 'mark' )
    if answer3 == "d":
        print('question-3', answer3,'is correct', + Tscore, 'marks')
    else:
        print('question-3', answer3, 'is not correct', + Tscore-Tscore, 'mark' )
    if answer4 == "a":
        print('question-4', answer4, 'is correct', + Tscore, 'marks')
    else:
        print('question-4', answer4, 'is not correct', + Tscore-Tscore, 'mark' )  
    if answer1 != 'c' and answer2 != 'b' and answer3 != 'd' and answer4 != 'a':
        print('Your chosen answer options are all invalid') 
    if answer1 == 'c' and answer2 == 'b' and answer3 =='d' and answer4 =='a':
        print("Your total score is:", + Tscore * 4, '\n' 'Your percentage score is:', + Tscore / 100 * 20, '\n' 'Cheerio!!!')
    elif answer1 == 'c' and answer2 == 'b' and answer4 == 'a':
        print("Your total score is:", + Tscore * 3, '\n' 'Your percentage score is:', + Tscore / 100 * 15, '\n' 'Cheerio!!!')
    elif answer2 == 'b' and answer3 == 'd' and answer4 == 'a':
        print("Your total score is:", + Tscore * 3, '\n' 'Your percentage score is:', + Tscore / 100 * 15, '\n' 'Cheerio!!!')
    elif answer1 == 'c' and answer3 == 'd' and answer4 == 'a':
        print("Your total score is:", + Tscore * 3, '\n' 'Your percentage score is:', + Tscore / 100 * 15, '\n' 'Cheerio!!!')
    elif answer1 == 'c' and answer2 == 'b':
        print("Your total score is:", + Tscore + Tscore, '\n' 'Your percentage score is:', + Tscore / 100 * 10, '\n' 'Cheerio!!!')
    elif answer1 == 'c' and answer3 == 'd':
        print("Your total score is:", + Tscore + Tscore, '\n' 'Your percentage score is:', + Tscore / 100 * 10, '\n' 'Cheerio!!!')
    elif answer3 == 'd' and answer4 == 'a':
        print("Your total score is:", + Tscore + Tscore, '\n' 'Your percentage score is:', + Tscore / 100 * 10, '\n' 'Cheerio!!!')
    elif answer2 == 'b' and answer4 == 'a':
        print("Your total score is:", + Tscore + Tscore, '\n' 'Your percentage score is:', + Tscore / 100 * 10, '\n' 'Cheerio!!!')
    elif answer1 == 'c' or answer2 == 'b' or answer3 == 'd' or answer4 == 'a':
        print("Your total score is:", + Tscore, '\n' 'Your percentage score is:', + Tscore / 100 * 5, '\n' 'Cheerio!!!')
    elif answer1 != 'c' or answer2 != 'b' or answer3 != 'd' or answer4 != 'a':
        print("Your total score is:", + Tscore-Tscore, '\n' 'Your percentage score is:', + Tscore / 100 * 0, '\n' 'Cheerio!!!')
my_question(quest = "1. Which of the following is a collective noun?" + '\n' "(a) beautiful (b) joyous (c) bunch  (d) goat" + '\n\n'
  "2. Which of the following is a pronoun?" + '\n' "(a) train (b) it (c) sinking ship (d) being " + '\n\n'
"3. Which of the following is a verb?" + '\n' "(a) train (b) it (c) sinking ship (d) being" + '\n\n'
"4. Which of the following is a preposition?" + '\n' "(a) under (b) dog (c) book (d) mine", Tscore = 5)



