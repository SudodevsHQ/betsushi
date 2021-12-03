from sqlalchemy import Column, DateTime, ForeignKey, String
from src.database.crud import Crud
from src.database.database import Base


# sqlalchemy models for upi
class UPI(Base, Crud):
    __tablename__ = 'upi'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    created_at = Column(DateTime)

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"created_at={self.created_at} "
        )
