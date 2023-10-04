# Normal BFS Traversal 

# model
model = {"S": ["A", "B", "C"],
         "A": ["S", "D"],
         "B": ["S", "E", "D", "G"],
         "C": ["S", "E"],
         "D": ["A", "F", "B"],
         "F": ["D", "G", "E"],
         "E": ["C", "F", "H", "B"],
         "H": ["E", "G"],
         "G": ["F", "B", "H"]
         }

initial = "S"
goal = "G"
frontier = [initial]
explored = []

count = 1
while frontier:
    value = frontier.pop(0)
    if value not in explored: 
        explored.append(value)
        if goal == value:
            break
        for val in model[value]:
            if val not in explored and val not in frontier:
                frontier.append(val)
        count+=1
print("BFS: ")               
print(explored)

# Normal DFS Traversal without Goal

initial_dfs = "S"
frontier_dfs = [initial_dfs]
explored_dfs = []
while frontier_dfs:
    value = frontier_dfs.pop()
    if value not in explored_dfs:
        explored_dfs.append(value)
        new_frontier_dfs = [val for val in model[value]
                        if val not in explored_dfs and val not in frontier_dfs][::-1]
        frontier_dfs.extend(new_frontier_dfs)
print("DFS: ")
print(explored_dfs)
