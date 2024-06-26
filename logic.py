from collections import deque
from utill.my_random import secure_random
import random

def distribute_people(total_people, num_teams):
        people_per_team = total_people // num_teams
        remainder = total_people % num_teams

        team_distribution = []

        for i in range(num_teams):
            if i < remainder:
                team_distribution.append(people_per_team + 1)
            else:
                team_distribution.append(people_per_team)

        return team_distribution
    
def rfs(lists: dict, num_teams: int, now_team: int = 0):
    key = lists.keys()
    key = list(key)
    queue = deque()
    visited = {i:False for i in key}
    team_list = [[] for i in range(num_teams)]
    team_distribution = distribute_people(len(key), num_teams)

    def now_team_update():
        nonlocal now_team
        now_team = secure_random(0, num_teams - 1)
        while len(team_list[now_team]) >= team_distribution[now_team]:
            now_team = (now_team + 1) % num_teams

    def append_to_team(i):
        nonlocal now_team
        if len(team_list[now_team]) < team_distribution[now_team]:
            team_list[now_team].append(i)
        else:
            now_team_update()
            team_list[now_team].append(i)

    while sum(visited.values()) < len(visited):
        if len(queue) == 0:
            start = random.choice([i for i in key if visited[i] == False])
            queue.append(start)
            visited[start] = True
            append_to_team(start)
        else:
            now = queue.popleft()
            for i in random.sample(lists[now], min(secure_random(0, len(lists[now]))+1 # if list is not empty
                                                   , len(lists[now]))): # if list is empty
            # for i in lists[now][:secure_random(0, len(lists[now]))+1]: # Priority can be applied
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    append_to_team(i)

    team_list.sort()
    for i in range(len(team_list)):
        team_list[i].sort()

    return team_list