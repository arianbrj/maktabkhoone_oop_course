import random as rd

rand_num = rd.randint(0,10)

guess_left = 3

def check_answer(answer):
    if answer > rand_num:
        return(False,"choose lower number")
    elif answer < rand_num:
        return(False,"choose bigger number")
    elif answer == rand_num:
        return(True,"Bingo")

name = input("enter your name: ").rstrip()
while True:
    if guess_left == 0:
        print(f"you ran out of guesses!\n answer was: {rand_num}")
        break

    answer_input = int(input(f"{name}, please enter your guess number: ").strip())
    answer_result = check_answer(answer_input)
    
    if answer_result[0] == False:
        print(answer_result[1])
    else:
        print(answer_result[1])
        break
    guess_left -= 1

print("end of the game")