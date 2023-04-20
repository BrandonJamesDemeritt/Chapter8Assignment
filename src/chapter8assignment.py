'''
Created on Oct 21, 2022

@author: Brandon Demeritt
'''


'''
(1) Prompt the user to input five pairs of numbers: A player's jersey number (0 - 99) and the player's rating (1 - 9). 
Store the jersey numbers and the ratings in a dictionary. Output the dictionary's elements with the jersey numbers in ascending order 
(i.e., output the roster from smallest to largest jersey number). Hint: Dictionary keys can be stored in a sorted list.

(2) Implement a menu of options for a user to modify the roster. Each option is represented by a single character. 
The program initially outputs the menu, and outputs the menu after a user chooses an option. 
The program ends when the user chooses the option to Quit. For this step, the other options do nothing.

(3) Implement the "Output roster" menu option.

(4) Implement the "Add player" menu option. Prompt the user for a new player's jersey number and rating. Append the values to the two vectors.

(5) Implement the "Delete player" menu option. Prompt the user for a player's jersey number. 
Remove the player from the roster (delete the jersey number and rating).

(6) Implement the "Update player rating" menu option. Prompt the user for a player's jersey number. 
Prompt again for a new rating for the player, and then change that player's rating.

(7) Implement the "Output players above a rating" menu option. Prompt the user for a rating. 
Print the jersey number and rating for all players with ratings above the entered value. 

'''
#Get initial 5 man roster of jerseys and ratings
numbers = {}
for i in range(5):
    jersey = int(input("Please enter player's %d Jersey number: " % (i+1)))
    rating = int(input("Please enter player's %d Rating: " %(i+1)))
    numbers[jersey]=rating


#convert dictionary to list to sort.
sortNumbers = list(numbers.items())
sortNumbers.sort()


#Print sorted roster
print("\nROSTER:")
for x in range(len(sortNumbers)):
    s = "Jersey Number: " + str(sortNumbers[x][0]) + ", Rating: " + str(sortNumbers[x][1])
    print(s)


#creating menu and initial variables
userChoice = "non"
menu = {
    "a" : "Output Roster",
    "b" : "Add Player",
    "c" : "Delete Player",
    "d" : "Update Player rating",
    "e" : "Output players above a rating",
    "q" : "Quit"
    }


#while loop for user actions
while userChoice != "q":
    print()
    for s, o in menu.items():
        print(s, "--->", o)
    userChoice = input("Please select what you want to do: ")
    
    #User action a, print roster
    if userChoice == "a":
        sortNumbers = list(numbers.items())
        sortNumbers.sort()
        print("ROSTER:")
        for x in range(len(sortNumbers)):
                s = "Jersey Number: " + str(sortNumbers[x][0]) + ", Rating: " + str(sortNumbers[x][1])
                print(s)
    
    #user action b, add player
    elif userChoice == "b":
        jersey = int(input("\nPlease enter new players Jersey number: "))
        if jersey in numbers:
            print("Sorry, that player already exists, did you mean to modify the rating?")
        else:
            rating = int(input("Please enter the new players rating: "))
            numbers[jersey] = rating
    
    #user action c, delete player
    elif userChoice == "c":
        jersey = int(input("\nPlease enter the player's jersey you wish to delete: "))
        numbers.pop(jersey, "Player not found") 
    
    #user action d, update player rating
    elif userChoice == "d":
        jersey = int(input("\nPlease enter the players Jersey number to modify: "))
        if jersey in numbers:
            rating = int(input("Please enter the players modified rating: "))
            numbers[jersey] = rating
        else:
            print("\nSorry, that player isn't the database, maybe you wanted to add a player?")    
    
    #user action e, output players above a certain rating
    elif userChoice == "e":
        rating = int(input("\nPlease enter the rating to show all players above: "))
        sortNumbers = list(numbers.items())
        sortNumbers.sort()
        print("\nPlayers above rating: " + str(rating) + ":")
        for i in range(len(sortNumbers)):
            if sortNumbers[i][1] > rating:
                print("Jersey number: " + str(sortNumbers[i][0]) + ", Rating: " + str(sortNumbers[i][1]))

    else:
        if userChoice != "q":
            print("\nSorry, that's not an option, try again.")

print("\n\nThe End")

