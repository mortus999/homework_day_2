#1. Nested Decisions: The Adventure Game 🏰
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

    #Task 2: Setting the Scene
#Based on the corrected code from Task 1, expand the game. If the user chooses "cave", 
#ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
if place == "cave":
    action=input("light a torch or procced in the dark")
    if action == "light a torch":
        print("you light the cave")
    else:
        print("proceed in the dark")
else:
    print ("please select cave or forest")


#2. Quick Decisions: The Event Planner 🎉
#Task 1: Code Correction
#You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
#Task 2: Venue Selection
#Based on the corrected code from Task 1,
#further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
audio_system= "audio system" if attendees >100 else "projector"
projector="projector" if attendees >100 else "none"
print(venue, audio_system, projector)
#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. 
#Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".


###############################################################################HOMEWORK 2##################################################################################################
#number = input(int("Enter a number: "))

#if number > 0:
#    print("The number is positive.")
#elif number == 0:
#    print("The number is zero.")
#else:
#    print("The number is negative.")


#  2. The Greatest Showdown
#Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. 
#The program should then identify and print out the largest number among the three.

num1= input("please type ur first number")
num2= input("please type ur second number")
num3= input("please type ur third number")
if num1 > num2 and num1 > num3:
    print("number 1 is the biggest number")
elif num2 > num1 and num2> num3:
    print("number 2 is the biggest number")
elif num3 > num1 and num3> num2:
    print("number three is bigger")

#Task 2: Identify the Smallest
#Extend your program from Task 1 to also 
#determine the smallest number among the three and print it out.
num1= int(input("please type ur first number"))
num2= int(input("please type ur second number"))
num3= int(input("please type ur third number"))

if num1 > num2 and num1 > num3:
    print("number 1 is the biggest number")
elif num2 > num1 and num2> num3:
    print("number 2 is the biggest number")
elif num3 > num1 and num3> num2:
    print("number three is bigger")
smallest_number="This is the smallest number"
if(num1 <= num2 and num1 <= num3):
    print(num1, "is the smallest")
 
elif(num2 <= num1 and num2 <= num3):
    print(num2, "is the smallest")
else:
    print(num3, "is the smallest")




