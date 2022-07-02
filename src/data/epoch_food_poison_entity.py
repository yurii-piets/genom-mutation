from src.data.config import Base
from sqlalchemy import Column, Integer


class EpochFoodPoisonEntity(Base):
    __tablename__ = 'epoch_food_poison'
    epoch = Column(Integer, primary_key=True)
    food_count = Column(Integer)
    poison_count = Column(Integer)

    def __init__(self, epoch, food_count, poison_count):
        self.epoch = epoch
        self.food_count = food_count
        self.poison_count = poison_count
