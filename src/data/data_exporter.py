from abc import abstractmethod

FILE_EPOCH_TICKS = "../data/epoch_ticks.csv"
FILE_BOT_EPOCH_TICKS = "../data/bot_epoch_ticks.csv"
FILE_EPOCH_FOOD_POISON = "../data/epoch_food_poison.csv"


class CsvDataExporter:
    def __init__(self):
        with open(FILE_EPOCH_TICKS, 'w') as file:
            file.write('')
        with open(FILE_BOT_EPOCH_TICKS, 'w') as file:
            file.write('')
        with open(FILE_EPOCH_FOOD_POISON, 'w') as file:
            file.write('')

    def save_epoch_ticks(self, epoch, ticks):
        with open(FILE_EPOCH_TICKS, 'a') as file:
            file.write(str(epoch) + ';' + str(ticks) + '\n')

    def save_bot_epoch_ticks(self, epoch, ticks):
        with open(FILE_BOT_EPOCH_TICKS, 'a') as file:
            file.write(str(epoch) + ';' + str(ticks) + '\n')

    def save_epoch_food_poison(self, epoch, food_amount, poison_amount):
        with open(FILE_EPOCH_FOOD_POISON, 'a') as file:
            file.write(str(epoch) + ';' + str(food_amount) + ';' + str(poison_amount) + '\n')
