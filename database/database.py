from .__init__ import engine
from sqlalchemy.orm import Session, sessionmaker
from .schema import Base


dbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    Base.metadata.create_all(bind=engine)
    db = dbSession()
    try:
        yield db
    finally:
        db.close()
