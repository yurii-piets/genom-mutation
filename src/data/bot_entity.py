from src.data.config import Base
from sqlalchemy import String, Column, Integer, ARRAY


class BotEntity(Base):
    __tablename__ = 'bots'
    id = Column(Integer, primary_key=True, autoincrement=True)
    energy = Column(Integer)
    direction = Column(String)
    genes = Column(ARRAY(Integer))
    created_epoch = Column(Integer)
    drop_epoch = Column(Integer)
    ticks = Column(Integer)

    def __init__(self, bot):
        if hasattr(bot, 'id'):
            self.id = bot.id
        self.energy = bot.energy
        self.direction = str(bot.direction)
        self.genes = bot.genes.genes
        self.created_epoch = bot.created_epoch
        if hasattr(bot, 'drop_epoch'):
            self.drop_epoch = bot.drop_epoch
        self.ticks = bot.ticks
