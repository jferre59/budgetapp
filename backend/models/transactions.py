from sqlalchemy import Column, Integer, String, Date, Numeric

from database import Base

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

    