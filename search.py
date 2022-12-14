# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    "*** YOUR CODE HERE ***"
    from util import Stack
    frontier = Stack()
    explored = []
    actions = []
    frontier.push((problem.getStartState(), []))

    while(not frontier.isEmpty()):
        coordinates, actions = frontier.pop()
        if problem.isGoalState(coordinates):
            return actions
        if coordinates not in explored:
            explored.append(coordinates)
            for i in problem.getSuccessors(coordinates):
                frontier.push(( i[0], (actions + [i[1]])))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    frontier = Queue()
    explored = []
    actions = []
    frontier.push((problem.getStartState(), []))

    while(not frontier.isEmpty()):
        coordinates, actions = frontier.pop()
        if problem.isGoalState(coordinates):
            return actions
        if coordinates not in explored:
            explored.append(coordinates)
            for i in problem.getSuccessors(coordinates):
                frontier.push(( i[0], (actions + [i[1]])))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue
    frontier = PriorityQueue()
    explored = []
    frontier.push((problem.getStartState(), []), 0)
    # if EMPTY?(frontier) then return failure
    while (not frontier.isEmpty()):
        # node <- POP(frontier)
        coordinates, actions = frontier.pop()
        # if problemGOAL-TEST(node.STATE) then return SOLUTION(node)
        if problem.isGoalState(coordinates):
            return actions
        if coordinates not in explored:
            # add node.STATE to explored
            explored.append(coordinates)
            for i in problem.getSuccessors(coordinates):
                # if child.STATE is not in explored or frontier
                if i[0] not in (state[2][0] for state in frontier.heap):
                    action = actions + [i[1]]
                    cost = problem.getCostOfActions(action)
                    # frontier <- INSERT(child, frontier)
                    frontier.push((i[0], action), cost)
                # if child.STATE is in frontier with higher PATH-COST
                else:
                    for j in frontier.heap:
                        if j[2][0] == i[0]:
                            cur_cost = problem.getCostOfActions(j[2][1])
                    new_cost = problem.getCostOfActions(actions + [i[1]])
                    # replace that frontier node with child
                    if cur_cost > new_cost:
                        action = actions [i[1]]
                        frontier.update((i[0], actions), new_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    frontier = PriorityQueue()
    explored = []
    frontier.push((problem.getStartState(), [], 0), 0)

    while (not frontier.isEmpty()):
        coordinates, actions, cost_now = frontier.pop()
        if problem.isGoalState(coordinates):
            return actions
        if coordinates not in explored:
            explored.append(coordinates)
            for coord_next, action_next, cost_next in problem.getSuccessors(coordinates):
                heuristics = cost_now + cost_next + heuristic(coord_next, problem)
                frontier.push((coord_next, (actions + [action_next]), (cost_now + cost_next)), heuristics)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
