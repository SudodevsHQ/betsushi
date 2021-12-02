from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric

from database.database import  async_db_session, Base
from database.crud import Crud

# sqlalchemy models for the account table
class Account(Base, Crud):
    __tablename__ = 'account'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Numeric)
    contact_id = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
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
