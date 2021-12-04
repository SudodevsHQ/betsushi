import enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, \
    Numeric
from src.database.database import Base
from src.database.crud import Crud
from datetime import date, datetime

class TransactionType(enum.Enum):
    send = "send"
    receive = "receive"


class TransactionStatus(enum.Enum):
    queued = "queued"
    rejected = "rejected"
    pending = "pending"
    processing = "processing"
    processed = "processed"
    cancelled = "cancelled"
    reversed = "reversed"


# sqlalchemy models for transaction
class Transaction(Base, Crud):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    razorpay_tid = Column(String)
    amount = Column(Numeric)
    user_id = Column(String, ForeignKey('users.id'))
    type = Column(Enum(TransactionType))
    fund_account_id = Column(String, nullable=True)
    upi = Column(String)
    status = Column(String)
    # status = Column(Enum(TransactionStatus))
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f"razorpay_tid={self.razorpay_tid}, "
            f"amount={self.amount}, "
            f"user_id={self.user_id}, "
            f"type={self.type}, "
            f"fund_account_id={self.fund_account_id}, "
            f"upi={self.upi}, "
            f"status={self.status}, "
            f"created_at={self.created_at} "
        )
