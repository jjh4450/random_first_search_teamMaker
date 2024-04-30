import datetime

def save_teams_to_file(team_list):
        with open(f'./output/teams{datetime.datetime.now()}.txt', 'w') as file:
            for i, team in enumerate(team_list):
                file.write(f"Team {i + 1}: {', '.join(team)}\n")