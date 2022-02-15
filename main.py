from art import logo
import random
print(logo)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


# def comparision(guess):
#     if guess > :


def levels():

    global total_chances

    print(f"You have {total_chances}attempts remaining to guess the number.")
    end_of_game = False
    the_no=[]

    the_no.append(number())
    print(the_no[0])
    c=the_no[0]
    while end_of_game == False:
        guess=int(input("Make a guess"))

        if guess<c:
            print("too low")
            total_chances -= 1
            end_of_game=False
        elif guess<c:
            print("too high ")
            total_chances -= 1
            end_of_game = False

        else:

            print(f"you win the number was {c}")

            end_of_game = True

            if total_chances==0:
                end_of_game=True




def number():
    numbers=[]

    for n in range(101):
        numbers.append(n)
    a=random.choice(numbers)
    # print(f"Correct answer is {a}")
    return a
number()


total_chances=0

difficulty=input(f"Choose a difficulty hard or easy ")
if difficulty == "easy":
    total_chances+=10
else:
    total_chances+=5


# print(total_chances)



levels()







