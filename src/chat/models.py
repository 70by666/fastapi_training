from sqlalchemy import Column, Integer, String, Table

from src.database import metadata

message = Table(
    'message',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('message', String),
)
