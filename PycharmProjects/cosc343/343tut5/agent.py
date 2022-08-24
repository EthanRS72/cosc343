from chess_board import chess_board
import random
import numpy as np
import math
import itertools

#init board
board = chess_board()

#init population with random chromosomes
c = [random.sample(range(0, 63), board.size) for i in range(10)]
#c = list(itertools.permutations(c))
#iterate over generations
while True:
    fitness_scores = []
    #iterate over individuals in population
    c_best = None
    best_score = 0
    for i in range(len(c)):
        #Evaluate fitness
        f = board.nonattacking_pairs(c[i])
        fitness_scores.append(f)
        if f > best_score:
            c_best = c[i]
            best_score = f
    #pick best and show board
    board.show_state(c_best)
    print("Current best is : ", best_score)

    #if fitness is 28 solution found otherwise continue to next generation
    if best_score == 28:
        break
    #for each new child
    for i in range(len(c)):
        if i == 0:
            child = c_best
            #else:
             #   ordered = c[:]
              #  ordered = sorted(ordered, reverse = True)
               # child = ordered[1]

        else:
            total = sum(fitness_scores)
            p = [f/total for f in fitness_scores]
            p1,p2 = np.random.choice(len(c), size=2, replace=False,p=p)
            p1 = c[p1]
            p2 = c[p2]
            half = math.floor(len(p1) / 2) + 2
            split = random.randint(1,7)
            #cross over parents to create new child
            child = list(p1)
            child[:half] = p2[:half]
            #random chance for mutation
            val = random.randint(1,100)
            if val > 1:
                mod = random.choice((1,2))
                for index in range(len(child)):
                    if index % mod == 0:
                        child[index] = random.randint(0,63)
        #replace population with new children
        c[i] = child


