from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
import sqlalchemy
import logging
import os
import traceback
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, exc, Sequence, UniqueConstraint , text
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.schema import CreateSchema

# Define the database URI
db_uri = 'postgresql://master:pass@localhost/GLOBBING'

# Create a database engine
engine = create_engine(db_uri)

# Connect to the database
with engine.connect() as conn:
    try:
        # Create the 'initial' schema if it doesn't exist
        conn.execute(CreateSchema('initial', if_not_exists=True))
        print("Initial schema created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the initial schema: {e}")


    __tablename__ = 'Facts'
    __table_args__ = {'schema': 'initial'}

    id = Column(Integer, primary_key=True)
    customer_id = Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)
    invoice_id = Column(String(50),unique= True, nullable=False)
    date = Column(DateTime, nullable=False)
    quantity = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)   
     