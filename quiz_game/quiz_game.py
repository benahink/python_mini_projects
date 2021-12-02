print("Welcome to my computer quiz!")

playing = input("Do you want to play? Y/N ")
if playing.lower() != "y":
    quit()

print("Okay! Let the game begin!")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")

# question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")

# question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")

# question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("That is incorrect.")

# def game():

#     # question 1
#     answer = input("What does CPU stand for? ")
#     if answer.lower() == "central processing unit":
#         print("Correct!")
#         score += 1
#     else:
#         print("That is incorrect.")

#     # question 2
#     answer = input("What does GPU stand for? ")
#     if answer.lower() == "graphics processing unit":
#         print("Correct!")
#         score += 1
#     else:
#         print("That is incorrect.")

#     # question 3
#     answer = input("What does RAM stand for? ")
#     if answer.lower() == "random access memory":
#         print("Correct!")
#         score += 1
#     else:
#         print("That is incorrect.")

#     # question 4
#     answer = input("What does PSU stand for? ")
#     if answer.lower() == "power supply":
#         print("Correct!")
#         score += 1
#     else:
#         print("That is incorrect.")


# while True:
#     game()
#     restart = input("do you want to restart Y/N?")
#     if restart.lower() == "n":
#         print("You final score is: " + str(score) + "/4")
#         print("Thank you for playing!")
#         break
#     elif restart.lower() == "y":
#         continue


print("You final score is: " + str(score) + "/4")
print("Thank you for playing!")
