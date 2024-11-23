from models import Player, Enemy
from exceptions import GameOver, EnemyDown
from settings import ATTACK_PAIRS_OUTCOME, WIN, LOSE, DRAW, POINTS_FOR_FIGHT, POINTS_FOR_KILLING, HARD_MODE_MULTIPLIER

class Game:
    def __init__(self, player, mode):
        self.player = player
        self.mode = mode
        self.enemy = self.create_enemy()

    def create_enemy(self):
        level = self.player.score // 10 + 1  
        return Enemy(level=level, mode=self.mode)

    def fight(self):
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        print(f"Вы выбрали: {player_attack}, соперник выбрал: {enemy_attack}")
        result = ATTACK_PAIRS_OUTCOME[(player_attack, enemy_attack)]
        return result

    def handle_fight_result(self, result):
        if result == WIN:
            print("Вы победили в этом раунде!")
            self.enemy.decrease_lives()
            self.player.add_score(POINTS_FOR_FIGHT)
        elif result == LOSE:
            print("Вы проиграли этот раунд!")
            self.player.decrease_lives()
        else:
            print('Ничья')
 
    def play(self):
        while True:
            try:
                result = self.fight() 
                self.handle_fight_result(result)
            except EnemyDown:
                print('Вы победили соперника!')
                self.player.add_score(POINTS_FOR_KILLING)
                self.enemy = self.create_enemy()
            except GameOver:
                print("Игра окончена. Вы проиграли.")
                self.save_score()
                break

    def save_score(self):
        from score import ScoreHandler
        handler = ScoreHandler()
        handler.add_player_score(self.player.name, self.mode, self.player.score)