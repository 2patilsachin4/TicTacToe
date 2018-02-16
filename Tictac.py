#importing modules
import random

#global constants
X = "X"
O = "O"
EMPTY = " "
display1 = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
place_holder1 = [0, 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
winning_sequence_lists = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
is_win = [False, False]

#Instructions for the game
def Instructions():
    """Display game instructions"""
    print \
    """

    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0-8. The number will
    correspond to the board position as illustrated:

      0 | 1 | 2
     -----------
      3 | 4 | 5
     -----------
      6 | 7 | 8

    Prepare yourself, human. The ultimate battle is about to begin. \n
    """

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response

def player_choice(place_holder):
    print \
    """

       0 | 1 | 2
      -----------
       3 | 4 | 5
      -----------
       6 | 7 | 8

    """

    response = None
    while response not in (place_holder):
        response = int(raw_input(place_holder))
    return response


def current_board_positions(display):
    """Displays the current position of the match when called."""
    print " ", display[0], " | ", display[1], " | ", display[2]
    print "\n ", display[3], " | ", display[4], " | ", display[5]
    print "\n ", display[6], " | ", display[7], " | ", display[8]


def first_move_who():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print "\nThen take the first move.You will need it. You will play with X's"
        human = X
        computer = O
    else:
        print "\nYour bravery will cost you man....I will go first then."
        computer = X
        human = O
    return computer, human


def is_legal_move(move):
    """Determines whether a move chosen by user is legal or not."""
    if display[place_holder[move]] != EMPTY:
        print "Not a legal move"
        return False
    else:
        return True



def tie():
    print "It was a tie player. Next time I will beat you."

    
def congrat_winner(is_win):
    if is_win[0]:
        print "How did this happen!!! I cannot lose. I will have my revenge next time player."
        return True
    if is_win[1]:
        print "I win Player!!Told you! I am invincible."
        return True
    else:
        return False


def player_movement(player_move,place_holder,p_steps,display,n,is_win):
    """Determines the next move of player and plays it."""
    response = player_choice(place_holder)
    player_move.append(response)
    place_holder.remove(player_move[p_steps])
    if n == 1:
        display[response] = X
    else:
        display[response] = O
    current_board_positions(display)
    if p_steps >=3:
        response2 = is_winning_player
        if response2[0] == True:
            is_win[0] = True
        
    
            


def computer_movement(place_holder, c_steps, computer_move,player_move,p_steps,n,display,is_win):
    """Determines the next move of computer and plays it."""
    if n == 2:
        computer = X
    else:
        computer = O
    if c_steps < n:
            computer_move.append(random.choice(place_holder1))
            display[computer_move[c_steps]] = computer  
            current_board_positions(display)
            place_holder.remove(computer_move[c_steps])
    
    else:
        #Attacking Sequence and win for Computer Sequence
        response = [None,[None]]
        response = is_winning(computer_move,place_holder)
        if response[0] == True:
            display[response[1][c_steps]] = computer
            current_board_positions(display)
            is_win[1] = True
            
                                 
        #Defense Sequence
        response2 = [None,[None]]
        response2 = is_defense_req(player_move,place_holder,p_steps)
        if response2[0] == True:
            display[response2[1][p_steps]] = computer
            if is_win[1] != True:
                current_board_positions(display)
            computer_move.append(response2[1][p_steps])
            place_holder.remove(player_move[p_steps])
            player_move.remove(response2[1][p_steps])

        #Random Sequence   
        if response[0]== False and response2[0] == False:
            computer_move.append(random.choice(place_holder))
            display[computer_move[c_steps]] = computer
            current_board_positions(display)
            place_holder.remove(computer_move[c_steps])

           



def is_winning_player(player_move):
    """Checks for winning sequence in player_move list."""
    for winning_sequence in winning_sequence_lists:
            if set(winning_sequence) <= set(player_move):
                return [True,player_move]
    return [False,[None]]


  
    
def is_winning(computer_or_player_list,place_holder):
    """Determines if the computer has to play a attacking sequence or not."""
    for place in place_holder:
        computer_or_player_list.append(place)
        for winning_sequence in winning_sequence_lists:
            if set(winning_sequence) <= set(computer_or_player_list):
                return [True,computer_or_player_list]
        computer_or_player_list.remove(place)
    return [False,[None]]



def is_defense_req(player_move,place_holder,p_steps):
    """Determines if the computer has to play a defensive sequence or not."""
    response2 = [None,[None]]
    response2 = is_winning(player_move,place_holder)
    if response2[0] == True:
        return response2
    else:
        return [False,[None]]

def value_of_n(first_move):
    if first_move[0] == X:
        n = 2
        return n
    else:
        n = 1
        return n


def main():
    """The main loop of the game."""
    #Variables to keep track of the progress of the game.
    global display1
    global place_holder1
    global is_win
    c_steps1 = 0
    computer_move1 = []
    player_move1 = []
    p_steps1 = 0
    t_steps1 = p_steps1 + c_steps1


    #Main Loop of the Game.
    Instructions()
    first_move = first_move_who()
    n = value_of_n(first_move)



    #A while loop to control the flow of repeated steps in the game.
    while len(place_holder1) > 0:
        if n == 1:
            player_movement(player_move1,place_holder1,p_steps1,display1,n,is_win)
            if is_win[0] == True:
                break
            p_steps1 = p_steps1 + 1
            if len(place_holder1) != 0:
                print "Now the computer will play its move."
                computer_movement(place_holder1, c_steps1, computer_move1,player_move1,p_steps1,n,display1,is_win)
                if is_win[1] == True:
                    break
                c_steps1 = c_steps1 + 1
                print "Common Player make your move now....."

        else:
            computer_movement(place_holder1, c_steps1, computer_move1,player_move1,p_steps1,n,display1,is_win)
            if is_win[1] == True:
                break
            c_steps1 = c_steps1 + 1
            if len(place_holder1) != 0:
                print "Common Player make your move now....."
                player_movement(player_move1,place_holder1,p_steps1,display1,n,is_win)
                if is_win[0] == True:
                    break
                p_steps1 = p_steps1 + 1
                print "Now the computer will play its move."
            
    congrat_winner(is_win)
    if congrat_winner == False:
        tie()


          


main()
raw_input("press the enter key to exit")



















