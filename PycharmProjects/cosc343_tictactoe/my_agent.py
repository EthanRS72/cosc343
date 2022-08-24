__author__ = "Lech Szymanski"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "lech.szymanski@otago.ac.nz"
__date__ = "July 2022"

# Import the random number generation library
import random
import helper

class TicTacToeAgent():
    """
           A class that encapsulates the code dictating the
           behaviour of the TicTacToe playing agent

           Methods
           -------
           AgentFunction(percepts)
               Returns the move made by the agent given state of the game in percepts
           """

    def __init__(self, h):
        """Initialises the agent

        :param h: Handle to the figures showing state of the board -- only used
                  for human_agent.py to enable selecting next move by clicking
                  on the matplotlib figure.
        """
        pass

    def minimax(self, depth, percepts, player):
        if depth == 0 or helper.terminal(percepts):
            return helper.evaluate(percepts)
        if player:
            value = -1000000
            for move in helper.remove_symmetries(helper.maxs_possible_moves(percepts)):
                value = max(value, self.minimax(depth - 1, move, False))
            return value
        else:
            value = 100000000
            for move in helper.remove_symmetries(helper.mins_possible_moves(percepts)):
                value = min(value, self.minimax(depth - 1, move, True))
            return value

    def AgentFunction(self, percepts):
        """The agent function of the TicTacToe agent -- returns action
         relating the row and column of where to make the next move

        :param percepts: the state of the board a list of rows, each
        containing a value of three columns, where 0 identifies the empty
        suare, 1 is a square with this agent's mark and -1 is a square with
        opponent's mark
        :return: tuple (r,c) where r is the row and c is the column index
                 where this agent wants to place its mark
        """
        best_value = -1000000
        new_move = None
        new_states = helper.remove_symmetries(helper.maxs_possible_moves(percepts))
        for s in new_states:
            value = self.minimax(6, s, False)
            if value > best_value:
                new_move = s
        r,c = helper.state_change_to_action(percepts,new_move)
        return r,c


















