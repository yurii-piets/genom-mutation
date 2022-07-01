from abc import abstractmethod


class DataExporter:
    @abstractmethod
    def save_epoch_ticks(self, epoch, ticks): ...

    @abstractmethod
    def save_bot_epoch_ticks(self, epoch, ticks): ...


FILE_NAME = "../../data/epoch_ticks.csv"
FILE_NAME2 = "../../data/bot_epoch_ticks.csv"


class CsvDataExporter(DataExporter):
    def __init__(self):
        with open(FILE_NAME, 'w') as file:
            file.write('')
        with open(FILE_NAME2, 'w') as file:
            file.write('')

    def save_epoch_ticks(self, epoch, ticks):
        with open(FILE_NAME, 'a') as file:
            file.write(str(epoch) + '|' + str(ticks) + '\n')

    def save_bot_epoch_ticks(self, epoch, ticks):
        with open(FILE_NAME2, 'a') as file:
            file.write(str(epoch) + '|' + str(ticks) + '\n')
