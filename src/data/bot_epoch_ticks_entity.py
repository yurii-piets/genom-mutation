from sqlalchemy import Column, Integer

from src.data.config import Base


class BotEpochTicksEntity(Base):
    __tablename__ = 'bot_epoch_ticks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    epoch = Column(Integer)
    ticks = Column(Integer)

    def __init__(self, epoch, ticks):
        self.epoch = epoch
        self.ticks = ticks
