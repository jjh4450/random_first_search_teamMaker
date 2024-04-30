import datetime

def save_teams_to_file(team_list):
        with open(f'./output/teams{datetime.datetime.now()}.txt', 'w') as file:
            for i, team in enumerate(team_list):
                file.write(f"Team {i + 1}: {', '.join(team)}\n")

import pandas as pd
def save_teams_to_excel(team_list):
    # 팀 데이터를 DataFrame으로 변환
    team_data = {}
    max_length = max(len(team) for team in team_list)
    for i, team in enumerate(team_list):
        team_data[f"Team {i + 1}"] = team + [''] * (max_length - len(team))
    
    df = pd.DataFrame(team_data)
    
    # 엑셀 파일로 저장
    file_name = f"./output/teams_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"File saved as {file_name}")