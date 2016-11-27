# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  #"*** YOUR CODE HERE ***"
  #util.raiseNotDefined()

  from game import Directions
  from util import Stack

  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  result = []
  visited = []
  solution = Stack()

  def _getX(state):
    if state == None: return None
    return state[0]
  def _getY(state):
    if state == None: return None
    return state[1]

  def _isVisited(state):
    if state == None: return None
    # REFATORAR: usar uma estrutura de acesso otimo 
    x, y = _getX(state), _getY(state)
    return (x,y) in visited

  def _getSuccessorsNotVisitedState(state):
    if state == None: return None
    return ([scs 
      for scs in problem.getSuccessors(state)
      if(not _isVisited(_getState(scs)))])

  def _getState(successor):
    if successor == None: return None
    return successor[0]

  def _visit(state):
    if state == None: return None
    visited.append(state)

  def _unvisit(state):
    if state == None: return None
    visited.remove(state)

  def _getDirection(successor):
    if successor == None: return None
    return successor[1]

#  def _getDirection(stateSrc, stateDst):
#    if stateSrc ==  stateDst == None: return None
#
#    xS, yS = stateSrc[0], stateSrc[1]
#    xD, yD = stateDst[0], stateDst[1]
#    if(xS > xD): return w
#    if(xS < xD): return e
#    if(yS > yD): return s
#    if(yS < yD): return n
#    return Directions.STOP

  def getPath(currentState):
    if currentState == None: return None

    _visit(currentState)
    if(problem.isGoalState(currentState)):
      return True
    else:
      for successor in _getSuccessorsNotVisitedState(currentState):
        if(getPath(_getState(successor))):
          solution.push(_getDirection(successor))
          return True
      _unvisit(currentState)
      return False
    #import pdb; pdb.set_trace()
    

  print
  print "######################"
  print

  getPath(problem.getStartState())
  import pdb; pdb.set_trace()
  result = []
  while(not solution.isEmpty()):
    result.append(solution.pop())

  print "isEmpty: "+ str(solution.isEmpty())
  print "SOLUTION: " + str(solution)
  print "RESULT: " + str(result)

  print
  print "######################"
  print

  return result

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch