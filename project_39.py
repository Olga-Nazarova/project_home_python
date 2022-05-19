# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

import random
def gamePlayers(volume):
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    queue = [player1, player2]
    print("Жеребьевка...")
    draw(queue)
    print(f'Первым ходить будет {queue[0]}')
    while volume > 0:
        print(f'Сейчас очередь игрока {queue[0]}')
        volume = play(volume)
        if volume == 0:
            print(f'Игрок {queue[0]} победил!')
        queue.reverse()

def gameBot(volume):
    player1 = input("Введите имя первого игрока: ")
    player2 = "Bot"
    queue = [player1, player2]
    print("Жеребьевка...")
    draw(queue)
    print(f'Первым ходить будет {queue[0]}')
    while volume > 0:
        print(f'Сейчас очередь игрока {queue[0]}')
        if queue[0] == "Bot":
            volume = botAction(volume)
        else:
            volume = play(volume)
        if volume == 0:
            print(f'Игрок {queue[0]} победил!')
        queue.reverse()

def botAction(volume):
    if volume <= 28:
        number = volume
    elif volume > 28 and volume <= 30:
        number = 1;
    elif volume == 31:
        number = 2
    elif volume == 32:
        number = 3
    elif volume == 33:
        number = 4
    elif volume == 34:
        number = 5
    elif volume == 35:
        number = 6
    elif volume == 36:
        number = 7
    elif volume == 37:
        number = 8
    elif volume == 38:
        number = 9
    elif volume == 39:
        number = 10
    elif volume == 40:
        number = 11
    elif volume == 41:
        number = 12
    elif volume == 42:
        number = 13
    elif volume == 43:
        number = 14
    elif volume == 44:
        number = 15
    elif volume == 45:
        number = 16
    elif volume == 46:
        number = 17
    elif volume == 47:
        number = 18
    elif volume == 48:
        number = 19
    elif volume == 49:
        number = 20
    elif volume == 50:
        number = 21
    elif volume == 51:
        number = 22
    elif volume == 52:
        number = 23
    elif volume == 53:
        number = 24
    elif volume == 54:
        number = 25
    elif volume == 55:
        number = 26
    elif volume == 56:
        number = 27
    elif volume == 57:
        number = 28
    elif volume > 57:
        number = random.randint(1, 29)

    volume -= number
    print(f'Bot забирает {number} конфет')
    print(f'На столе осталось {volume} конфет')
    return volume

def play(volume):
    while True:
        col = int(input("Сколько конфет вы хотите взять со стола? \n"))
        if col <= volume and col <= 28:
            volume -= col
            break
        else:
            print('Нельзя забрать больше конфет, чем их есть на столе и больше, чем 28 штук. Попробуйте ещё раз!')
    print(f'На столе осталось {volume} конфет')
    return volume

def draw(queue):
    if random.randint(1, 2) == 1:
        return queue
    else:
        queue.reverse()
        return queue

vol = 2021

while True:
    getGame = int(input("Введите 1, чтобы играть с реальным игроком или 2 чтобы играть с ботом: "))
    if getGame == 1:
        gamePlayers(vol)
        break
    if getGame == 2:
        gameBot(vol)
        break
    else:
        print('Ввод некорректен. Попробуйте снова')