from sqlalchemy import create_engine , String , Integer , Float ,Column
from sqlalchemy.orm import Session , sessionmaker , DeclarativeBase


DATABASEURL = "sqlite///./test.db"

engine = create_engine(DATABASEURL , connect_args = {"check_same_thread": False})

Base = DeclarativeBase()

class DBModel():
    __tablename__ = "abc"

    id = Column(Integer , primary_key = True , index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind = engine
)

def get_db():
    db = SessionLocal()

    try : yield db 
    finally: db.close()


class UserModel():
    name : str
    email : str
    password : str
    age : int

