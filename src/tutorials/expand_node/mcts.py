#
# MCTS algorithm implementation
#

# packages
import math
import random

# tree node class definition
class TreeNode():
    # class constructor (create tree node class instance)
    def __init__(self, board, parent):
        # init associated board state
        self.board = board
        
        # init is node terminal flag
        if self.board.is_win() or self.board.is_draw():
            # we have a terminal node
            self.is_terminal = True
        
        # otherwise
        else:
            # we have a non-terminal node
            self.is_terminal = False
        
        # init is fully expanded flag
        self.is_fully_expanded = self.is_terminal
        
        # init parent node if available
        self.parent = parent
        
        # init the number of node visits
        self.visits = 0
        
        # init the total score of the node
        self.score = 0
        
        # init current node's children
        self.children = {}

# MCTS class definition
class MCTS():
    # search for the best move in the current position
    def search(self, initial_state):
        # create root node
        self.root = TreeNode(initial_state, None)

        # walk through 1000 iterations
        for iteration in range(1000):
            # select a node (selection phase)
            node = self.select(self.root)
            
            # scrore current node (simulation phase)
            score = self.rollout(node.board)
            
            # backpropagate results
            self.backpropagate(node, score)
        
        # pick up the best move in the current position
        try:
            return get_best_move(self.root, 0)
        
        except:
            pass
    
    # select most promising node
    def select(self, node):
        # make sure that we're dealing with non-terminal nodes
        while not node.is_terminal:
            # case where the node is fully expanded
            if node.is_fully_expanded:
                node = self.get_best_move(node, 2)
            
            # case where the node is not fully expanded 
            else:
                # otherwise expand the node
                return self.expand(node)
       
       # return node
       return node
    
    # expand node
    def expand(self, node):
        # generate legal states (moves) for the given node
        states = node.board.generate_states()
        
        # loop over generated states (moves)
        for state in states:
            # make sure that current state (move) is not present in child nodes
            if str(state.position) not in node.children:
                # create a new node
                new_node = TreeNode(state, node)
                
                # add child node to parent's node children list (dict)
                node.children[str(state.position)] = new_node
                
                # case when node is fully expanded
                if len(states) == len(node.children):
                    node.is_fully_expanded = True
                
                # return newly created node
                return new_node
        
        # debugging
        print('Should not get here!!!')
    
    # simulate the game via making random moves until reach end of the game
    def rollout(self, board):
        pass
    
    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, score):
        pass
    
    # select the best node basing on UCB1 formula
    def get_best_move(self, node, exploration_constant):
        # define best score & best moves
        best_score = float('-inf')
        best_moves = []
        
        # loop over child nodes
        for child_node in node.children.values():
            # define current player
            if child_node.board.player_2 == 'x': current_player = 1
            elif child_node.board.player_2 == 'o': current_player = -1
            
            # get move score using UCT formula
            move_score = current_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(math.log(node.visits / child_node.visits))                                        
            print('move_score:', move_score)
            # better move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]
            
            # found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)
            
        # return one of the best moves randomly
        return random.choice(best_moves)




























