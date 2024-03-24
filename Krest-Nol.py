# Нолики-крестики

board = list(range(1, 10))  # Генерируем список

def view_table(board):
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player):
    valid = False
    while not valid:
        questions = input("Выберите клетку: ")
        try:
            questions = int(questions)
        except ValueError:
            print("Нужно ввести число")
            continue
        if 1 <= questions <= 9:
            if str(board[questions - 1]) not in "XO":
                board[questions - 1] = player
                valid = True
            else:
                print("Клетка занята")
        else:
            print("Неправильный ввод. Введите число 1-9")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        view_table(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        check = check_win(board)
        if check:
            print(check, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    view_table(board)


main(board)