from eightpuzzle import eightpuzzle
import time



class node:
    def __init__(self, s, parent=None, g=0, h=0, action=None):
        self.s = s
        self.parent = parent
        self.g = g
        self.f = g+h
        self.action = action


def heuristic(s,goal):
    h = 0
    for i in range(len(s)):
        for x in range(len(goal)):
            if s[i] == goal[x]:
                h = h + abs(x-i)
    return h


start_time = time.time()
puzzle = eightpuzzle(mode = "easy")
init_state = puzzle.reset()
goal_state = puzzle.goal()

root_node = node(s=init_state,parent=None, g=0,h=heuristic(s=init_state, goal=goal_state))
fringe = [root_node]
closed_list = []
solution_node = None

print("Searching for solution")
while len(fringe) > 0:
    current_node = fringe.pop(0)
    closed_list.append(current_node)
    current_state = current_node.s
    if current_state == goal_state:
        solution_node = current_node
        break
    else:
        available_actions = puzzle.actions(s=current_state)
        for a in available_actions:
            next_state = puzzle.step(s=current_state, a=a)
            if not (a in closed_list):
                new_node = node(s=next_state,
                                parent=current_node,
                                g=current_node.g+1,
                                h=heuristic(s=next_state, goal=goal_state),
                                action=a)
                fringe.append(new_node)
        fringe.sort(key=lambda  x: x.f)

if solution_node is None:
    print("No solution found")
else:
    action_sequence = []
    next_node = solution_node
    while True:
        if next_node == root_node:
            break

        action_sequence.append(next_node.action)
        next_node = next_node.parent
    action_sequence.reverse()
    elapsed_time = time.time() - start_time
    print("Solution found in %d moves" % solution_node.g)
    print("Time taken: %.3f seconds" % elapsed_time)
puzzle.show(s=init_state, a=action_sequence)
