from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric

from database.database import  async_db_session, Base
from database.crud import Crud

# sqlalchemy models for upi
class UPI(Base, Crud):
    __tablename__ = 'upi'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'))
    created_at = Column(DateTime)
    
    __mapper_args__ = {"eager_defaults": True}
    
    def __repr__(self):
            return (
                f"<{self.__class__.__name__}("
                f"id={self.id}, "
                f"user_id={self.user_id}, "
                f"created_at={self.created_at} "
            )

