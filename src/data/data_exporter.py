import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.bot_entity import BotEntity
from src.data.bot_epoch_ticks_entity import BotEpochTicksEntity
from src.data.config import Base
from src.data.epoch_food_poison_entity import EpochFoodPoisonEntity
from src.data.epoch_ticks_entity import EpochTicksEntity


class PsqlDataExporter:
    def __init__(self):
        engine = create_engine(
            'postgresql://gn_usr:' + os.getenv('GENOM_MUTATION_PASSWORD') + '@localhost:5432/genom_mutation')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        Base.metadata.create_all(engine)

    def save_epoch_ticks(self, epoch, ticks):
        self.session.add(EpochTicksEntity(epoch=epoch, ticks=ticks))
        self.session.commit()

    def save_bot_epoch_ticks(self, epoch, ticks):
        self.session.add(BotEpochTicksEntity(epoch=epoch, ticks=ticks))
        self.session.commit()

    def save_epoch_food_poison(self, epoch, food_count, poison_count):
        self.session.add(EpochFoodPoisonEntity(epoch=epoch, food_count=food_count, poison_count=poison_count))
        self.session.commit()

    def save_bot(self, bot):
        if hasattr(bot, 'id'):
            return bot.id
        entity = BotEntity(bot)
        self.session.add(entity)
        self.session.commit()
        return entity.id

    def update_bot(self, bot):
        entity = BotEntity(bot)
        self.session.merge(entity)
        self.session.commit()
        return entity.id
