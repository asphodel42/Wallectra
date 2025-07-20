from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, declarative_base
import enum
from datetime import datetime

Base = declarative_base()


class TransactionType(enum.Enum):
    topup = "topup"
    withdraw = "withdraw"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(Enum("admin", "user"), default="user")

    wallet = relationship("Wallet", uselist=False, back_populates="user")


class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'),
                     unique=True, nullable=False)
    balance = Column(Numeric(10, 2), default=0.00, nullable=False)

    user = relationship("User", back_populates="wallet")
    transactions = relationship(
        "Transaction", back_populates="wallet", cascade="all, delete-orphan")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(String(255))
    created_at = Column(
        DateTime, default=datetime.now(tz="UTC"), nullable=False)

    wallet = relationship("Wallet", back_populates="transactions")
