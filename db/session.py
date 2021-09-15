from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:admin@localhost:3306/film_zone',
    pool_pre_ping=True,
    pool_recycle=3600,
)
Session = sessionmaker(bind=engine, autocommit=False)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
