from game import Game
from score import ScoreHandler
from models import Player
from settings import MODES

def create_player():
    name = input("Введите ваше имя: ")
    print("Выберите уровень сложности:")
    print("1 - Normal")
    print("2 - Hard")
    while True:
        difficulty = input("Выберите (1 или 2): ")
        if difficulty in MODES:
            mode = MODES[difficulty]
            break
        print("Неверный выбор. Попробуйте снова.")
    return Player(name), mode
def play_game():
    player, mode = create_player()
    game = Game(player, mode)
    game.play()

def show_scores():
    handler = ScoreHandler()
    handler.display()

def main():
    while True:
        print("1 - Начать игру")
        print("2 - Показать очки")
        print("3 - Выйти")
        choice = input("Выберите действие (1, 2, 3): ")
        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == '__main__':
    main()