from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from src.database.crud import Crud
from src.database.database import Base
from sqlalchemy.future import select

from src.database.database import async_db_session

# sqlalchemy models for the account table
class Account(Base, Crud):
    __tablename__ = "account"

    id = Column(String, primary_key=True)
    balance = Column(Numeric)
    contact_id = Column(String)
    user_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime)

    # required in order to acess columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f"balance={self.balance}, "
            f"contact_id={self.contact_id}, "
            f"user_id={self.user_id}, "
            f"created_at={self.created_at} "
        )
