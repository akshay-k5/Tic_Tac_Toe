
#Project info function
def info():
    print("_"*20,"AI COURSE PROJECT","_"*20)
    print("PROJECT NAME: Tic tac toe using Mini-Max Algorithm") 
    print(">TEAM_MEMBERS")
    members=["Aswin M","P Suraj Prasanth","Akshay Kumar KS","Vaishnav B Ajith"]
    for i in members:
        print("-->"+i)
    print()

#Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row)) #To create barrier "|"
        print("-" * 9)
    print()


#Check if someone has won
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":  # Row win
            return board[i][0]                                
        if board[0][i] == board[1][i] == board[2][i] != " ":   # Column win
            return board[0][i]  
    if board[0][0] == board[1][1] == board[2][2] != " ":    # Diagonal win
        return board[0][0]  
    if board[0][2] == board[1][1] == board[2][0] != " ":     # Diagonal win
        return board[0][2]  
    return None

# Check if the board is full
def is_full(board):
    return all([cell != " " for row in board for cell in row])      #Returns True /False 

#______________________________________________EVALUATING_ALGORITHM______________________________________________________________

# Minimax algorithm
def minimax(board, depth, is_ai_turn):
    winner = check_winner(board)
    if winner == "O":                     #AI wins
        return 10 - depth
    if winner == "X":                    #Player wins
        return depth - 10
    if is_full(board):                   # Draw
        return 0

    if is_ai_turn:
        max_eval = float("-inf")        #-alpha,minus infinity max
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    val = minimax(board, depth + 1, False)  #Recursive function call
                    board[i][j] = " "
                    max_eval = max(max_eval, val)
        return max_eval
    else:
        min_eval = float("inf")        #+beta,plus infinity min 
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    val= minimax(board, depth + 1, True)    #Recursive function call 
                    board[i][j] = " "
                    min_eval = min(min_eval, val) 
        return min_eval

# AI chooses the best move using Minimax
def minimax_ai_move(board):
    bestscore = float("-inf")
    bestmove = None
    for i in range(3):         #Iteration loop for Row
        for j in range(3):     #Iteration loop for Column
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False) 
                board[i][j] = " "
                if score > bestscore:
                    bestscore = score
                    bestmove = [i, j]    #BEST MOVE
    return bestmove                      #Returns best move for AI in list format

#___________________________________________________________Main game loop____________________________________________________________________
def tic_tac_toe():
    print("______Welcome to Tic-Tac-Toe!______\n")
    board = [[" " for i in range(3)] for i in range(3)] # Board creation 3x3 matrix statement nested list
    print(">Instruction\n>>You are X and AI is O.")
    print_board(board)

    while True:
        # Player's turn
        try:
            move = input("Enter your move (row and column, e.g., 1 2): ")
            row, col = map(int, move.split())
            if board[row-1][col-1] != " ":
                print("Cell already taken. Try again.")
                continue
            board[row-1][col-1] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        print("\nYour move:")
        print_board(board)

        # Check if player wins
        if check_winner(board) == "X":
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI's move:")
        ai_move = minimax_ai_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
        print_board(board)

        # Check if AI wins
        if check_winner(board) == "O":
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Start the game
tic_tac_toe()
