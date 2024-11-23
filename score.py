from settings import SCORE_FILE, MAX_RECORDS_NUMBER

class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name} ({self.mode}) - {self.score}"

class GameRecord:
    def __init__(self):
        self.records = []       

    def add_record(self, record):
        for existing_record in self.records:
            if existing_record.name == record.name and existing_record.mode == record.mode:
                if existing_record.score < record.score:
                    existing_record.score = record.score
                return
        self.records.append(record)

    def prepare_records(self):
        self.records.sort(reverse = True)
        self.records = self.records[:MAX_RECORDS_NUMBER]

class ScoreHandler:
    def __init__(self):
        self.game_record = GameRecord()
        self.file_name = SCORE_FILE
        self.read()

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    try:
                        name, mode, score = line.strip().split(',')
                        score = int(score) 
                        self.game_record.add_record(PlayerRecord(name, mode, score))
                    except ValueError:
                        print(f"Ошибка: неверный формат данных в строке: {line.strip()}")
        except FileNotFoundError:
            print(f"Файл {self.file_name} не найден.")

    def save(self):
        self.game_record.prepare_records()
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(f"{record.name},{record.mode},{record.score}\n")

    def display(self):
        print("Текущие результаты:")       
        if not self.game_record.records:
            print("Нет записей.")          
        else:
            for record in self.game_record.records: 
                print(record)     

    def add_player_score(self, name, mode, score):
        self.game_record.add_record(PlayerRecord(name, mode, score))
        self.save()