import os
import time
def print_title():
    print("""
 ____      _    _   _ ____   ___  __  __   _____ ___ ____  ____ _____ 
|  _ \    / \  | \ | |  _ \ / _ \|  \/  | |  ___|_ _|  _ \/ ___|_   _|
| |_) |  / _ \ |  \| | | | | | | | |\/| | | |_   | || |_) \___ \ | |  
|  _ <  / ___ \| |\  | |_| | |_| | |  | | |  _|  | ||  _ < ___) || |  
|_|_\_\/_/__ \_\_| \_|____/ \___/|_| _|_| |_|   |___|_| \_\____/ |_|  
/ ___|| ____|  / \  |  _ \ / ___| | | |
\___ \|  _|   / _ \ | |_) | |   | |_| |
 ___) | |___ / ___ \|  _ <| |___|  _  |
|____/|_____/_/   \_\_| \_\\____|_| |_|
 _____ _____  ___  ___  ___ ___  ___  ___   _   __ ___________ 
|_   _|  ___|/ _ \ |  \/  | |  \/  | / _ \ | | / /|  ___| ___ \\
  | | | |__ / /_\ \| .  . | | .  . |/ /_\ \| |/ / | |__ | |_/ /
  | | |  __||  _  || |\/| | | |\/| ||  _  ||    \ |  __||    /
  | | | |___| | | || |  | | | |  | || | | || |\  \| |___| |\ \\
  \_/ \____/\_| |_/\_|  |_/ \_|  |_/\_| |_/\_| \_/\____/\_| \_|
""")
    
def print_done():
    print("""
______ _____ _   _  _____ _ 
|  _  \  _  | \ | ||  ___| |
| | | | | | |  \| || |__ | |
| | | | | | | . ` ||  __|| |
| |/ /\ \_/ / |\  || |___|_|
|___/  \___/\_| \_/\____/(_)
      _               _      _   _              
  ___| |__   ___  ___| | __ | |_| |__   ___     
 / __| '_ \ / _ \/ __| |/ / | __| '_ \ / _ \    
| (__| | | |  __/ (__|   <  | |_| | | |  __/    
 \___|_| |_|\___|\___|_|\_\  \__|_| |_|\___|    
  ___  _   _| |_ _ __  _   _| |_   / _(_) | ___ 
 / _ \| | | | __| '_ \| | | | __| | |_| | |/ _ \\
| (_) | |_| | |_| |_) | |_| | |_  |  _| | |  __/
 \___/ \__,_|\__| .__/ \__,_|\__| |_| |_|_|\___|
                |_|                             

""")
    
def print_done_lol():
    print("""
  _    ___  _    
 | |  / _ \| |   
 | |_| (_) | |__ 
 |____\___/|____|   _                           _                  _ 
 |_   _| |_ (_)___ (_)___  _  _ ___ _  _ _ __  | |_ ___ __ _ _ __ | |
   | | | ' \| (_-< | (_-< | || / _ \ || | '__| |  _/ -_) _` | '  \|_|
   |_| |_||_|_/__/ |_/__/  \_, \___/\_,_|_|     \__\___\__,_|_|_|_(_)
                           |__/           
""")
    
def clear_console():
    print('\n'*100)
    os.system('clear')

def print_result_as_table(team_list, time_taken=0):
    max_name_length = max([max(len(member) for member in team) if team else 0 for team in team_list], default=0)
    column_width = max(max_name_length, 5)

    # 헤더 준비
    headers = ["TEAM {}".format(i+1) for i in range(len(team_list))]
    header_row = "\t".join(header.center(column_width) for header in headers)
    time.sleep(time_taken)
    print(header_row)
    time.sleep(0.8 if time_taken > 0 else 0)
    print("-" * (len(headers) * (column_width + 1) - 1))  # 구분선 출력

    # 최대 팀 길이 계산
    max_team_length = max(len(team) for team in team_list)

    # 각 행에 대해
    for i in range(max_team_length):
        row = []
        for team in team_list:
            if i < len(team):
                row.append(team[i].center(column_width))
            else:
                row.append(" " * column_width)
        time.sleep(time_taken)
        print("\t".join(row))
        time.sleep(0.8 if time_taken > 0 else 0)
        if i < max_team_length - 1:
            print("-" * (len(headers) * (column_width + 1) - 1))  # 각 행 사이에 구분선 출력
