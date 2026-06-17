from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, DateTime

from database import Base
from datetime import datetime

class Transaction(Base):
    """Model for a financial transaction."""

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    account_type = Column(String(20))

    transaction_date = Column(Date)

    merchant_name = Column(String(255))

    debit = Column(Numeric(12, 2))
    credit = Column(Numeric(12, 2))

    category = Column(String(100))

    year = Column(Integer)

    month = Column(Integer)

    is_income = Column(Boolean, default=False)

    is_subscription = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    