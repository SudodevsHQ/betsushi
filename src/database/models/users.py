from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.database import  async_db_session, Base
from database.crud import Crud

class User(Base, Crud):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    currency = Column(String(3))
    created_at = Column(DateTime)

    # required in order to acess columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
    
    def __repr__(self):
            return (
                f"<{self.__class__.__name__}("
                f"id={self.id}, "
                f"full_name={self.full_name}, "
                f"posts={self.currency}, "
                f"created_at={self.created_at}, "
                f")>"
            )
