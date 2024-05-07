# Random First Search Team Maker
  ![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
  <br>
This Python project is an advanced team maker designed to intelligently distribute participants into teams, considering preferences for specific teammates, thereby enhancing collaboration and satisfaction.

## Features
- **User Input**: Accepts names of participants and desired number of teams.
- **Intelligent Team Creation**: Distributes participants considering their preferences to maximize the likelihood of pairing with desired teammates.
- **Result Saving**: Outputs the created team configurations to a text file.

## How to Use
1. Run the script `rfs_teamMaker.py`.
2. Input participant names and type 'done' when finished.
3. Specify the desired number of teams.
4. Teams are generated with a consideration of user preferences, and results are saved.

## Algorithm Explanation
### Adjacency List Usage
The `rfs` function employs an adjacency list represented by a Python dictionary (`lists`) to manage the participants' preferences. This data structure allows each participant to list their preferred teammates, forming a network of preferences that the algorithm uses to create teams.

### Team Assignment Logic
Within the `rfs` function, the following line plays a crucial role in the team formation process:

```python
for i in random.sample(lists[now], min(random.randint(0, len(lists[now]))+1, len(lists[now]))):
    ...
```

- **Dynamic Selection**: It dynamically selects a subset of the participant's preferred teammates to consider for team assignment. This approach simulates real-life scenarios where preferences impact team formations but must adapt to others' availability and choices.
- **Random Sampling**: The `random.sample()` function randomly picks preferences, ensuring that the team assignments are influenced by user preferences yet maintain an element of unpredictability.
- **Flexible Size Handling**: The `min(...)` function ensures that the sample size is never larger than the number of available preferences, preventing errors and adapting to the size of the preference list.

### Queue-Based Distribution
The algorithm uses a queue (`deque`) to manage the processing of participants in a breadth-first manner, which helps evenly distribute participants across teams according to the structured preferences.

## Requirements
- Python 3.x

## Developer
- Contact: [jjh4450git@gmail.com](mailto:jjh4450git@gmail.com)

## License
- BSD 2-Clause License
