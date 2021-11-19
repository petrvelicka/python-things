# Tic-Tac-Toe 3x3 game

game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

players = ["X", "O"]
current_player = 0

GAME_CONTINUES = -1
DRAW = -2
# if a player won, number of that player is returned

def print_state(game_state):
    for line in range(3):
        print(*game_state[line], sep=" | ")
        # the abobe is the same as print(game_state[0], game_state[1], game_state[2]).
        # sep="something" is used for the separator between individual variables
        if line != 2: # don't print on the last line
            print("--+---+--")

# move return True if the move is correct and was added to the board and 0
def move():
    try:
        move = input("Input your move (format L C): ").split(" ") # we get a string a split it up into two numbers3
        line, column = int(move[0]), int(move[1])
        
        if not 0 <= line < 3:
            print("Error: invalid line")
            return False

        if not 0 <= column < 3:
            print("Error: invalid column")
            return False

        if game[line][column] != " ":
            print("Error: already taken")
            return False
        
        game[line][column] = players[current_player]
        return True
    except:
        print("Error: invalid input")
        return False

    return True

def win(game_state):
    # lines
    for line in game_state:
        if line[0] == line[1] == line[2] and line[0] != " ": # all three are of the same color and not empty
            if line[0] == players[0]:
                return 0
            else:
                return 1
    
    # columns
    for i in range(3):
        if game_state[0][i] == game_state[1][i] == game_state[2][i] and game_state[2][i] != " ":
            if game_state[0][i] == players[0]:
                return 0
            else:
                return 1

    # diagonals
    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[1][1] != " ":
        if game_state[0][0] == players[0]:
            return 0
        else:
            return 1
    if game_state[2][0] == game_state[1][1] == game_state[0][2] and game_state[1][1] != " ":
        if game_state[0][0] == players[0]:
            return 0
        else:
            return 1

    # check if draw
    isDraw = True
    for line in game_state:
        for square in line:
            if square == " ":
                isDraw = False
                break

    if isDraw:
        return DRAW
    else:
        return GAME_CONTINUES

# game loop
while win(game) == GAME_CONTINUES:
    print("Now plays player {}".format(current_player + 1))

    while not move(): # we wait until the user inputs a valid move
        pass          # pass means "do nothing"

    print_state(game)

    current_player += 1
    if current_player > 1:
        current_player = 0

result = win(game)

if result == DRAW:
    print("DRAW")
else:
    print("Player {} ({}) won! Congratulations".format(result + 1, players[result]))
