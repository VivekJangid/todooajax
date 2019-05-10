from sqlalchemy import Integer, Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
SQL_FILE = "mysql+pymysql://vivek:password@localhost:3306/flask"


class Description(Base):
    __tablename__ = 'Description'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))

    def __init__(self, name, description):
        self.name = name
        self.description = description


class SessionFactoryPool:
    current_session = None

    @staticmethod
    def get_curret_session():
        if SessionFactoryPool.current_session is None:
            session = SessionFactoryPool.create_new_session()
            SessionFactoryPool.current_session = session

        return SessionFactoryPool.current_session

    @staticmethod
    def create_new_session():
        database_engine = create_engine(SQL_FILE)
        Base.metadata.create_all(database_engine)
        Base.bind = database_engine

        session = sessionmaker()
        session.configure(bind=database_engine)

        return session()
