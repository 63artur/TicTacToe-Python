print("Tic Tac Toe")
user1 = input("Enter your name: ")
user2 = input("Enter your name: ")
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
user1_history = []
user2_history = []
winning_combinations = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]
turn = True
game = True
while game:
    print("\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "     1 | 2 | 3")
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "     4 | 5 | 6")
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "     7 | 8 | 9")
    print("\n")
    for combination in winning_combinations:
        if game_board[combination[0]] == "X" and game_board[combination[1]] == "X" and game_board[
            combination[2]] == "X":
            print(f'{user1} wins!')
            game = False
            break
        elif game_board[combination[0]] == "O" and game_board[combination[1]] == "O" and game_board[
            combination[2]] == "O":
            print(f'{user2} wins!')
            game = False
            break

    if not game:
        break
    if turn:
        print(f'Its {user1} turn!')
    else:
        print(f'Its {user2} turn!')
    if len(user1_history) == 5 and len(user2_history) == 5:
        print('End of game! No one win!')
        break
    print('Enter your choice:')
    choice = input()
    if choice in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        if turn:
            user1_history.append(choice)
            game_board[int(choice) - 1] = "X"
        else:
            user2_history.append(choice)
            game_board[int(choice) - 1] = "O"
        turn = not turn


