def greet():
    print("Приветствуем вас")
    print("    в игре      ")
    print("крестики-нолики ")
    print("----------------")
    print("формат ввода: x y")
    print("X - номер строки ")
    print("y - номер столбца")

def show():# Показ чистого поля
    print(f"  0 1 2")
    for i in range(3):
        print(f"{ i } { field[ i ][ 0 ] } { field[ i ] [ 1 ]} { field[ i ] [ 2 ]}")#Выводим поле

def ask():# Создаем проверку вводимых координат
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print('Введите 2 координаты')
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите число')
            continue
        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else :
                print('Клетка занята')
        else:
            print('Координаты вне диапазона')
        return x, y

def win():#Прописываем выйгрышные комбинации
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
           ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print("Выйграл", field[a[0]][a[1]])
            return True
    return False

greet()

field = [[" ", " ", " ", ] for i in range(3)]
num = 0

while True:# Создаем условие при котором ходяти Х или 0. Считаем ходы, если 9 ходов то ничья.
    num += 1
    show()
    if num % 2 ==1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"

    if win():# Если выйграшная комбинация прерываем игру
        break

    if num == 9:# Если 9 ходов прерываем игру
        print("Ничья")
        break