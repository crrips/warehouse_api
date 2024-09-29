from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


database_url = 'postgresql://user:secret@localhost:5432/warehouse_db'
engine = create_engine(database_url)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        