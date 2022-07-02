from sqlalchemy import Column, Integer

from src.data.config import Base


class EpochTicksEntity(Base):
    __tablename__ = 'epoch_ticks'
    epoch = Column(Integer, primary_key=True)
    ticks = Column(Integer)

    def __init__(self, epoch, ticks):
        self.epoch = epoch
        self.ticks = ticks
