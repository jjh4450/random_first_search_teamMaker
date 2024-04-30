from utill.console import *
from utill.file import save_teams_to_file, save_teams_to_excel
from logic import rfs


if __name__ == "__main__":
    print_title()
    print("Welcome to the Random First Search Team Maker!")
    print("Enter the names of the players and the number of teams you want to make.")
    print("When you're done, type 'done' to finish.")
    print()

    players = []
    while True:
        player = input("Enter a player's name: ")
        if player == "done":
            break
        players.append(player)

    num_teams = int(input("Enter the number of teams you want to make: "))

    dict_teams = {i:[] for i in players}
    for i in players:
        clear_console()
        print_title()
        print(f"{i} come here! and choose a teammate that you want")
        print(f"Here are the list of players: {players}")
        print("When you're done, type 'done' to finish.")
        while True:
            teammate = input(f"Enter a teammate's name: ")
            if teammate == "done":
                break
            elif teammate == i:
                print("You can't choose yourself as a teammate. Please choose another player.")
            elif teammate in dict_teams[i]:
                print("You've already chosen that player as a teammate. Please choose another player.")
            elif teammate not in players:
                print("That player is not in the list of players. Please choose a player from the list.")
            elif teammate in players:
                dict_teams[i].append(teammate)
            else:
                print("That player is not in the list of players. Please choose a player from the list.")
    clear_console()
    
    print_done()
    print("Here are the teams:")
    team_list = rfs(dict_teams, num_teams)
    
    save_teams_to_file(team_list)
    save_teams_to_excel(team_list)
    print("The teams have been saved to a file.")

    if "yes" == input("Do you want to see the teams in the console? (yes/no): "):
        if "yes" == input("Do you want to clear the console? (yes/no): "):
            clear_console()
        print_done_lol()
        print_result_as_table(team_list, 1.5)