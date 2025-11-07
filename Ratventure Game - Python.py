# Name: Hugo Von Louwen Dorosan
# School I.D.: S10202923D
# Class: IT01/P09
# This programme runs the game "Ratventure"

from random import randint

# +------------------------
# | Text for various menus
# +------------------------
main_text = ["New Game",
             "Resume Game",
             "Exit Game",
             "View Leaderboard"]

town_text = ["View Character",
             "View Map",
             "Move",
             "Rest",
             "Save Game",
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K'],]


# Side_orb_locations and common_orb_locations contain the possible locations for the orb
# Locations at the side of the map are in the same list to enhance similar probability
side_orb_locations = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], \
                     [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6]]

common_orb_locations = [[0, 4],[0, 5], [0, 6], [0, 7],\
                       [1, 4], [1, 5], [1, 6], [1, 7],\
                       [2, 4], [2, 6], [2, 7],\
                       [3, 4], [3, 5], [3, 6], [3, 7],\
                       [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7],\
                       [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],\
                       [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7]]


print("Welcome to Ratventure!")
print("----------------------")

# Code your main program here

# Name - Variable that stores the user's name of their character in the game
# Player - Variable that stores the user's icon in the game's map
# Damge - A list that contains the range of attacks the user is able to do
# Defence - A list that updates with new Defence ratings once certain movements in the game are done
# HP - A list taht updates with new Health points ratings once certain movements in the game are done
# Orb Location - A variable that stores the co-ordinates of the possible location of the orb
# day - A list that appends by 1 and updates every time a certain move i s done
# orb - A list indicating whether the user has posession of the orb
# game - Variable that appends another item and updates the list once game is completed
Name = "The Hero"
Player = "H"
Damge= [2, 3, 4]
Defence = [1]
HP = [20]
col_pos_recent = [0]
row_pos_recent = [0]


# randomized_orb() randomizes the location of the orb on the map
# to ensure side orbs have equal probability, only a certain number of variable "a" will result
# in a location from the sides to be selected
def randomized_orb():
    a = randint(0, 10)
    if a < 3:
        b = randint(0, len(side_orb_locations) - 1)
        orb_location = side_orb_locations[b]
    else:
        b = randint(0, len(common_orb_locations) - 1)
        orb_location = common_orb_locations[b]
    return orb_location
orb_location = randomized_orb()
day = [0]
x = 0
y = 0
orb = ["False"]
game = [1]

# main_menu()
# 1) Prints out the main menu's contents, found in the "main_text" list by using a for loop
# 2) The variable, "menu_choice", asks for user's input on which option from the main menu he chooses
# 3) Hence, "return menu_choice" stores the value in which the user may have keyed in
# 4) Afterwards, the "choice option" while loop uses the value stored in "menu_choice" and deploys the necessary functions
def main_menu():
    for a in range(len(main_text)):
        print("{}) {}".format(a + 1, main_text[a]))
    menu_choice = input("Enter Choice: ")
    return menu_choice

# player_stats()
# 1) Player stats display the user's Name, Damage range, Defence and current HP
# 2) Variables are stored at the top of the list and are updated once the user makes a certain game move
def player_stats():
    print(f"\nName: {Name}\nDamage: {Damge[0]} to {Damge[-1]}\nDefence: {Defence[-1]}\nHP: {HP[-1]}\n")


# option_one(day) - Town Menu
# 1) Prints out the town menu's contents, found in the "town_text" list by using a while loop
#   b) While loop was used so that this menu will repeat once user has done their specific move
#      within the town
#    to take while within the town
# 2) However, before the running the programme, list checks whether len(game) is more than 2 using for loop
#   b) variable, "game", contains a list that will be updated once the game ends
#   c) Hence, when the game ends, without asking for input, option_one_choice = 7 automatically,
#      causing the game to end
# 3) Depending on the input given by the user, the respective functions from the other lists will be called upon
# 4) Under option_one_choice == 3, an if else statement is used to check whether the move requested by the user
#    is causing the game character to move out of the game map in "world_map"
#    b) Henceforth, the character retains current co-ordinates, does not move, calls the required functions to show map

def option_one(day):
    option_one_choice = 0
    # option_one_choice - variable that asks for user's input on which choice they choose.
    # the programme converts the input from string to int as well
    while option_one_choice != 6 and option_one_choice != 5:

        #This if/else statement is used to check whether game has ended through checking a list "game" that will be
        #updated upon the defeat of the rat king
        if len(game) < 2:
            for a in range(len(town_text)):
                print("{}) {}".format(a + 1, town_text[a]))
            option_one_choice = int(input("Enter Choice: "))
        elif len(game) >= 2:
            option_one_choice = 7

        # option_one_choice == 1 displays the user's current statistics

        # option_one_choice == 2 displays Map of the user's player's whereabouts on the Game Map

        # option_one_choice == 3 asks user's input on which directions he wants to go and displaying the map afterwards

        # option_one_choice == 4 regenerates user's "HP" back to 20
        # col_pos_recent.append(col_pos_recent[-1]  row_pos_recent.append(row_pos_recent[-1])
        # Above list amendments to increase another day as the no of days = the number of items inside the lists
        # Both lists must be appended as column values = row

        # option_one_choice == 5 saves the game for the user by saving the map and co-ordinates by writing in a
        # File labeled: "saved_games.txt".
        # Hence, the programme asks user if they choose to Quit or Resume
        # This is done through an input variable called "resume_choice"
        # Using a while loop, options are displayed
        # resume_choice == 1, the co-ordinates are added on the col_pos_recent list and row_pos_recent list
        # resume_choice == 2, the player leaves the game, with the game map and co-ordinates saved. Therefore
        # leading user to home page (main_menu)

        # option_one_choice == 6, when user inputs '6', the programme exits the game and goes to home page
        # option_one_choice == 7, this variable only gets '7' once rat king has been defeated. Hence, ending the game
        # These two options were seperated to avoid confusion between ending the game through choice or ending the game
        # when the rat king gets defeated.

        if option_one_choice == 1:
            option_one_cone()
        elif option_one_choice == 2:
            option_one_ctwo(col_pos_recent, row_pos_recent)
        elif option_one_choice == 3:
            a = option_one_cthree(col_pos_recent, row_pos_recent)
            if a[0] > len(world_map) - 1 or a[1] > len(world_map) - 1:
                print("You cannot exit the map!")
                col_pos_recent.append(col_pos_recent[-1])
                row_pos_recent.append(row_pos_recent[-1])
            else:
                col_pos_recent.append(int(a[0]))
                row_pos_recent.append(int(a[1]))
            print(f"col: {col_pos_recent}\nrow:{row_pos_recent}")
            option_one_ctwo(col_pos_recent, row_pos_recent)
        elif option_one_choice == 4:
            HP.append(20)
            print(f"You have regenerated to full {HP[-1]} HP")
            col_pos_recent.append(col_pos_recent[-1])
            row_pos_recent.append(row_pos_recent[-1])
        elif option_one_choice == 5:
            path = "D:\School\Year 1.1\Programming I\Week 15\\"
            file = open(path + "saved_games.txt", "w")
            file.write(f"{str(col_pos_recent[-1])} {str(row_pos_recent[-1])}")
            file.close()
            print("Game Saved")
            resume_choice = -1
            while resume_choice != 1 or resume_choice != 2:
                resume_choice = int(input("1) Resume\n2) Quit\n Choose: "))
                if resume_choice == 1:
                    a = option_two()
                    col_pos_recent.append(int(a[0]))
                    row_pos_recent.append(int(a[1]))
                    print(col_pos_recent, row_pos_recent)
                    option_one(day)
                elif resume_choice == 2:
                    check_file()
                    break

        elif option_one_choice == 6 or option_one_choice == 7:
            print("Thank you for playing!\nYou may start a new game or Exit the game!\n")
            break

    # option_one_choice is returned so that this input value can be used to call certain functions to carry out the game
    return option_one_choice

# option_one_cone() - Displays the user's details by getting the variables: "Name", "Damge", "Defence", "HP"
def option_one_cone():
    print(f"\nName: {Name}\n    Damage: {Damge[0]} to {Damge[-1]}\n     Defence: {Defence}\n    HP: {HP[-1]}\n")


# option_one_ctwo() - Displays the Map in the current state of the game
# This shows the whole layout of the map, the location of towns, Rat King and user

# Variables 'a', 'b' and 'plyr' saves the structure of the map through text

# Using a nested for loop, The map is displayed through:
# 1) Printing out the borders and cells
# 2) Retrive the most current co-ordinates of players throught the col_pos_recent and row_pos_recent lists
# 3) Using the values to dispay the player's whereabouts on "world_map"

# Afterwards, the co-ordinates are checked through another if/else statement on whether they are on a 'Town',
# 'Open Space' or 'Rat King'
# The respective texts are saved in 'text' variable and called upon when required
# When in the open or against the rat king, respective functions, "attack(HP)" and "rat_king()" are called
def option_one_ctwo(col_pos_recent, row_pos_recent):
    a = "+---"
    b = "|"
    plyr = "H"
    for i in range(len(world_map)):
        print(len(world_map) * a + "+")
        for j in range(len(world_map)):
            k = world_map[j][i]
            if int(row_pos_recent[-1]) == j and int(col_pos_recent[-1]) == i:
                if k == ' ':
                    k = plyr
                    print(f'{b} {k} ', end="")
                elif k == 'T':
                    k = plyr + '/T'
                    print(f'{b}{k}', end="")
                elif k == 'K':
                    k = plyr + '/K'
                    print(f'{k}{b}', end="")
            print('| {} '.format(world_map[j][i]), end="")
        print("|")
    print(len(world_map) * a + '+')
    day = len(col_pos_recent)
    if world_map[col_pos_recent[-1]][row_pos_recent[-1]] == 'T':
        text = "You are in a town"
        print(f"Day {day}: {text}")
    elif world_map[col_pos_recent[-1]][row_pos_recent[-1]] == 'K':
        text = "You have encountered.. RAT KING!!!"
        print(f"Day {day}: {text}")
        rat_king()
    elif world_map[col_pos_recent[-1]][row_pos_recent[-1]] == ' ':
        text = "You are out in the open"
        print(f"Day {day}: {text}")
        attack(HP)

# option_one_cthree - moves the user's character through the input variable, "move_option"
# move_option is a variable that stores text, more specifically, "W", "A", "S" and "D"
# programme asks for input from user for Directions.
# "W" moves the user up by one cell, "A" moves the user left by one cell, "S" moves the user down by one cell,
# "D" moves the user right by one cell
# The current value in the col_pos_recent list will be added by one and stored in either col_pos or row_pos
# depending on whether the user moves through the column or through the row
# Hence, the value in col_pos or row_pos will be added into the list, updating the current whereabouts of the user
# This function returns variables "col_pos" and "row_pos" so that the required ammendments can be made when
# updating the new map

def option_one_cthree(col_pos_recent, row_pos_recent):
    move_option = 0
    col_pos = int(col_pos_recent[-1])
    row_pos = int(row_pos_recent[-1])
    print("\nDirections\nW: up, A: left, S: down, D: right\n")
    while move_option != "W" or move_option != "A" or move_option != "S" or move_option != "D":
        move_option = input("Your move: ")
        if move_option.capitalize() == "W":
            col_pos = int(col_pos_recent[-1]) - 1
            break
        elif move_option.capitalize() == "A":
            row_pos = int(row_pos_recent[-1]) - 1
            break
        elif move_option.capitalize() == "S":
            col_pos = int(col_pos_recent[-1]) + 1
            break
        elif move_option.capitalize() == "D":
            row_pos = int(row_pos_recent[-1]) + 1
            break

    return [col_pos, row_pos]

# attack(HP) - displays the attack menu when user is out in the open and afterwards,
# asks for the next move through the attack menu

def attack(HP):
# 'attack' variable takes a value that is randomised from 0 to the amount of damages possible in the Damge list
# Then, the value of the attack variable value will get a respective value from the list of damages from the Damge list
# Hence, the new_health value will calculate a user's new health by minusing the most recent health on the HP list off
# from the recent danage
# option == 1, is converted to int to make it a number in the programme, attacks the rat and afterwards, indicate how
# much attack is done and whether the player is victorious
# option == 2, is converted to int to make it a number in the programme, runs away from the rat, does not kill the rat
# but instead hides and proceedes to the attack menu
    attack = randint(0, len(Damge) - 1)
    new_health = HP[-1] - int(Damge[attack])
    HP.append(new_health)
    print("You have encountered... RATS!")
    print(f"Ouch! The Rat hit you for {Damge[attack]} damage")
    print(f"\nDamage: {Damge[0]} to {Damge[-1]}\nDefence: {Defence[-1]}\nHP: {HP[-1]}")
    print(f"You have {HP[-1]} HP left")
    option = 0
    while option != 1 or option != 2:
        option = input("1)Attack\n2)Run\nEnter choice: ")
        if int(option) == 1:
            print(f"\nYou dealt {Damge[attack]} damage to the rat")
            print("You are Victorious!!!!\n")
            break
        elif int(option) == 2:
            print("\nYou ran and hid from the rats")
            break

# 'option_2' is a variable that asks for input on which move the user wants to do in the attack menu options through a
# nested loop code consisting of while, for loops and if/else statements
    option_2 = 0
    print("1) View Character\n2) View Map\n3) Move\n4) Sense Orb\n5) Exit Game")
    while option_2 > 1 or option_2 < 5:
        option_2 = int(input("Enter choice: "))
        if option_2 == 1:
            # option_2 == 1, the player's current statistics will be displayed and the attack menu will be showed again
            player_stats()
            break
        elif option_2 == 2:
            # option_2 == 2, this displays the user's current whereabouts on the Game map by getting the recent values
            # from the col_pos_recent list and row_pos_recent list

            # Variables 'a', 'b' and 'plyr' saves the structure of the map through text

            # Using a nested for loop, The map is displayed through:
            # 1) Printing out the borders and cells
            # 2) Retrive the most current co-ordinates of players throught the col_pos_recent and row_pos_recent lists
            # 3) Using the values to dispay the player's whereabouts on "world_map"
            plyr = "H"
            a = "+---"
            for i in range(len(world_map)):
                print(len(world_map) * a + "+")
                for j in range(len(world_map)):
                    k = world_map[j][i]
                    if int(row_pos_recent[-1]) == j and int(col_pos_recent[-1]) == i:
                        if k == ' ':
                            k = plyr
                            print(f'| {k} ', end="")
                        elif k == 'T':
                            k = plyr + '/T'
                            print(f'|{k}', end="")
                        elif k == 'K':
                            k = plyr + '/K'
                            print(f'{k}|', end="")
                    print('| {} '.format(world_map[j][i]), end="")
                print("|")
            print(len(world_map) * a + '+')
            break
        elif option_2 == 3:
            # option_2 == 3, calls the function option_one_cthree(col_pos_recent, row_pos_recent) and saves this list in "a"
            # An if/else statement is used to check whether the move requested by the user is causing the game character
            # to move out of the game map in "world_map"
            # This is done by checking if the player's requested direction's co-ordinates are lesser than the amount of
            # cells given per column or row
            # The character retains current co-ordinates, does not move, calls the required functions to show the map
            # Code will continue if co-ordinates are within acceptable range
            a = option_one_cthree(col_pos_recent, row_pos_recent)
            if a[0] > len(world_map) - 1 or a[1] > len(world_map) - 1:
                print("You cannot exit the map!")
                col_pos_recent.append(col_pos_recent[-1])
                row_pos_recent.append(row_pos_recent[-1])
            else:
                col_pos_recent.append(int(a[0]))
                row_pos_recent.append(int(a[1]))
            option_one_ctwo(col_pos_recent, row_pos_recent)
            break
        elif option_2 == 4:
            # option_ 2 == 4, will append the recent co-ordinates to increase the day
            # checks whether option variable in attack menu has been "1"/"1) Run" through an if/else statement
            # - if previous option had chosen "run", programme will not allow user to sense orbs even if there is an orb
            # - if previous option had chosen "attack", programme will allow user to sense orbs
            # next, the programe checks if the current co-ordinates have any orbs of power on the map by:
            # 1) identifying whether current values in col_pos_recent and row_pos_recent lists are equal to the orb
            # location co-ordinates
            # 2) a) If location has orbs of power, an increment variable of value "5" is established
            #       Then, Damge list/HP list and Defence list will update its most recent Health point, Defence and
            #       Damage range by 5
            #    b) If location does not have orbs of power, a statement will display whether its close or not by taking
            #       the value of current co-ordinates and subtracting them off the co-ordinates of orb location
            col_pos_recent.append(col_pos_recent[-1])
            row_pos_recent.append(row_pos_recent[-1])
            if int(option) == 2:
                print("You are not able to sense any orb or power. You ran too much")
                break
            if int(option) == 1:
                if col_pos_recent[-1] == orb_location[0] and row_pos_recent[-1] == orb_location[1]:
                    print("\nYou found the ORB OF POWER!!!")
                    print(f"Your attack has increased by 5")
                    a = Damge[0] + 5
                    b = Damge[1] + 5
                    c = Damge[2] + 5
                    Damge.clear()
                    Damge.append(a)
                    Damge.append(b)
                    Damge.append(c)
                    print(f"Your defence increases by {increment}")
                    d = Defence[-1] + increment
                    Defence.append(d)
                    orb.append("True")
                else:
                    if col_pos_recent[-1] - orb_location[0] == 4 and row_pos_recent[-1] - orb_location[-1] == 4:
                        print("\nYou can sense that the Orb of Power is nearby!\n")
                    else:
                        print("\nNo Orb of Power can be sensed!")
                break
            break
        elif option_2 == 5:
            # This option ends the game and brings the user back to main menu page by calling the main_menu() function
            print("Exiting Game...")
            main_menu()
            break

# rat_king() - The whole fighting process between the user and rat king
def rat_king():
    # varible rat_king_defence and lists rat_king_damage and rat_king_HP take down the values of the current status
    # of the rat king
    # print statements are displayed afterwards
    # option variable asks for input value of which option the user chooses in the rat king attack menu using a while loop
    # if the recent string, the orb's is "true" (orb[-1] == True), user is able to cause damage to rat king
    # if the recent string , the orb's is "false", user will be unable to cause damage to rat king
    # this attack carries on until the rat_king_HP[-1] == 0
    # During the fight, print statements will be displayed updating the rat king's and user's status
    # Hence, a print statement will be displayed announcuing the end of the game and main menu function (main_menu())
    # will be called.

    rat_king_damage = [8, 9, 10, 11, 12]
    rat_king_defence = 5
    rat_king_HP = [25]
    option = 0
    while option != 1 or option != 2:
        print(f"\nDay {day}: You have encountered the Rat King!")
        print("Rat King")
        print(f"   Damage: {rat_king_damage[0]}-{rat_king_damage[-1]}")
        print(f"   Defence: {rat_king_defence}")
        print(f"   HP: {rat_king_HP}")
        if rat_king_HP == 0:
            print("The Rat King is dead! You are victorius!")
            print("Congratulations, you have defeated the Rat King!")
            print("The world is saved! You win!!!")
            game.append(0)
            break
        else:
            option = input("1)Attack\n2)Run\nEnter choice: ")
            a = randint(rat_king_damage[0], rat_king_damage[-1])
            b = randint(Damge[0], Damge[-1])
            if int(option) == 1:
                if orb[-1] == "True":
                    print("You have the Orb of Power!")
                    print(f"You deal {b} damage to the Rat King")
                    new_rk_health = rat_king_HP[-1] - b
                    rat_king_HP.append(new_rk_health)
                    print(f"Ouch! The Rat King hit you for {a} damage!")
                    new_health = HP[-1] - a
                    HP.append(new_health)
                    player_stats()
                    if rat_king_HP == 0:
                        print("The Rat King is dead! You are victorious!")
                        print("Congratulations, you have defeated the Rat King!")
                        print("The world is saved! You win!")
                        game.append(0)
                        # Once the game has ended, the following statistics(recent days and Name) are saved into a text
                        # This is to be opened later if user chooses to see previous' game scores
                        path = "D:\School\Programming I\Week 15\\"
                        file = open(path + "leaderboards.txt", "w")
                        file.write(f"{Name} {str(day[-1])} ")
                        file.close()
                    else:
                        continue
                else:
                    print("You do not have the Orb of Power - Rat King is immune")
                    print("You deal 0 damage to the rat")
                    print(f"OOF! The Rat King has hit you for {a} damage!")
                    new_health = HP[-1] - a
                    HP.append(new_health)
                    print(f"You have {new_health} HP left")
                    player_stats()
            elif int(option) == 2:
                print("\nYou ran and hid from the Rat King")
                break

# leaderboards() - displays the leaderboard which contains the ranking of previous' games no. of days completed
# "Leaderboards.txt" file is open and read.
# Values within the files are saved by appending into name and no_of_days list
# Using a for loop, the leaderboard is displayed
def leaderboards():
    name = []
    no_of_days = []
    path = "D:\School\Year 1.1\Programming I\Week 15\\"
    file = open(path + "leaderboards.txt", "r")
    for i in file:
        scores = i.split()

    name.append(scores[0])
    no_of_days.append(scores[1])
    print("{:>5s} {:>13s} {:>20s}".format("Player Name", "Rank", "No. of Days"))
    print(50 * "=")
    for i in range(-1, len(name) - 1):
        i += 1
        print("{:>7s} {:>15d} {:>20d}".format(name[i], i, days[i]))

# option_two() - resuming the game by saving its current map and the co-ordinates of the user
# A file, "saved_games.txt" is read and its contents are split into a list through a for loop.
# The contents of that list are returned and saved to allow the respective functions to continue the game
def option_two():
    path = "D:\School\Year 1.1\Programming I\Week 15\\"
    file = open(path + "saved_games.txt", "r")
    for cords in file:
        a = cords.split()
    return a

# check_file() - checks whether a map and co-ordinates were saved from any previous game
# This is in relation to the third option on main_menu()
# Programme checks whether file has the required data by reading the file
# Hence, if there are not contents, programme will display, "No game has been resumed"
# Otherwise, the game resumes where it was left off by calling the respective functions
def check_file():
    path = "D:\School\Year 1.1\Programming I\Week 15\\"
    file = open(path + "saved_games.txt", "r")
    if file.readline == None:
        print("\nWelcome Back!\n")
        option_one(day)
    else:
        print("\nNo game has been resumed\n")

# choice variable is originally 0 but upon calling the main_menu() function,
# the option is brought over and therefore, the respective functions are called
# to cater to the options chosen by the user

# choice == "1" starts the new game by displaying the stats and game

# choice == "2" resumes the game ONLY if file, "saved_games.txt" contains so

# choice == "3" ends the game and displays a farewall text

# choice == "4" displays the leaderboard of the previous games, showing the name, ranking position and no of days
#               taken to complete
choice = 0
while choice != "1" or choice != "2":
    choice = main_menu()
    if choice == "1":
        player_stats()
        option_one(day)
    elif choice == "2":
        check_file()
    elif choice == "4":
        leaderboards()
    elif choice == "3":
        print("\nThank you for playing!\n")
        break
