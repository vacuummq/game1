import random
from settings import PLAYER_LIVES, ALLOWED_ATTACKS, ATTACK_PAIRS_OUTCOME, WIN, LOSE, DRAW
from exceptions import GameOver, EnemyDown

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0

    def select_attack(self):
        while True:
            attack = input("Выберите атаку (1 - Бумага, 2 - Камень, 3 - Ножницы): ")
            if attack in ALLOWED_ATTACKS:
                return ALLOWED_ATTACKS[attack]
            print("Неверный выбор. Попробуйте снова.")

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def add_score(self, points):
        self.score += points

class Enemy:
    def __init__(self, level, mode):
        self.level = level
        if mode == 'Normal':
            self.lives = 3  
        elif mode == 'Hard':
            self.lives = 5  
        else:
            self.lives = 1  
            
    def select_attack(self):
        return random.choice(list(ALLOWED_ATTACKS.values()))

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown
        
