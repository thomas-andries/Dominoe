# Write your code here
import random


# creating the initial list
def set_starting_set():
    starting_dominoes = []
    for x in range(7):
        for y in range(7-x):
            starting_dominoes.append([x, y + x])
    random.shuffle(starting_dominoes)
    return starting_dominoes


# picking the dominoes, popping them out of the initial list, into the new list.
def picking_dominoes(dominoes):
    player_stack = []
    computer_stack = []
    for domino_counter in range(7):
        player_stack.append(dominoes.pop(random.randrange(0, len(dominoes))))
        computer_stack.append(dominoes.pop(random.randrange(0, len(dominoes))))
    return (player_stack, computer_stack, dominoes)


# check who has the highest domino
def highest_domino(player_stack, computer_stack, stock_pieces):
    domino_snake = []
    highest = [0, 0]
    found = False
    for domino_counter in range(7):
        if player_stack[domino_counter][0] == player_stack[domino_counter][1]:
            domino_snake.append([player_stack[domino_counter][0], player_stack[domino_counter][1]])
        elif computer_stack[domino_counter][0] == computer_stack[domino_counter][1]:
            domino_snake.append([computer_stack[domino_counter][0], computer_stack[domino_counter][1]])
    while found == False:
        if domino_snake[0][0] < domino_snake[1][0]:
            domino_snake.pop(0)
            if len(domino_snake) == 1:
                found = True
        elif domino_snake[0][0] > domino_snake[1][0]:
            domino_snake.pop(1)
            if len(domino_snake) == 1:
                found = True
    if domino_snake[0] in player_stack:
        pair = "player"
        index = player_stack.index(domino_snake[0])
        player_stack.pop(index)
    elif domino_snake[0] in computer_stack:
        pair = "computer"
        index = computer_stack.index(domino_snake[0])
        computer_stack.pop(index)
    else:
        dominoes = stock_pieces + player_stack + computer_stack
        test = picking_dominoes(dominoes)
        result = highest_domino(test[0], test[1], test[2])
        return (result[0], result[1], result[2], result[3], result[4])
    return (stock_pieces, computer_stack, player_stack, domino_snake, pair)


dominoes = set_starting_set()
test = picking_dominoes(dominoes)
result = highest_domino(test[0], test[1], test[2])
result_output = "Stock pieces: " + str(result[0]) + "\n"
result_output += "Computer pieces: " + str(result[1]) + "\n"
result_output += "Player pieces: " + str(result[2]) + "\n"
result_output += "Domino snake: " + str(result[3]) + "\n"
result_output += "Status: " + result[4]

print(result_output)





