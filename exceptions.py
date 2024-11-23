class GameOver(Exception):
    def __init__(self, message="Игра окончена. У вас закончились жизни."):
        self.message = message
        super().__init__(self.message)
        
class EnemyDown(Exception):
    def __init__(self, message="Соперник повержен."):
        self.message = message
        super().__init__(self.message)