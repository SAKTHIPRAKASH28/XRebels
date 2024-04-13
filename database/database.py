from .__init__ import engine
from sqlalchemy.orm import Session, sessionmaker
from .schema import Base


dbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = dbSession()
    try:
        yield db
    finally:
        db.close()
