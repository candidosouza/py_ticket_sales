from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.settings import Settings


class SQLAlchemyConfig:
    def get_engine(self):
        return create_engine(Settings().DATABASE_URL)

    @staticmethod
    def get_session():  # sourcery skip: raise-from-previous-error, raise-specific-error
        try:
            with Session(SQLAlchemyConfig().get_engine()) as session:
                return session
        except Exception as e:
            raise Exception(f'Error: {e}')
