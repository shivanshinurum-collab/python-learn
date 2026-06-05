from fastapi import Depends
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import column , String , Integer , Float , create_engine
from sqlalchemy.orm import sessionmaker , declarative_base , Session

dbURL = "sqlite:///./test.db"

engine = create_engine(dbURL , connect_args={"check_same_thread" : False})
Base = declarative_base()


class tableModel(Base):
    __tablename__ = "check"

    id = Column(Integer , primary_key=True , index= True)
    name = Column(String)
    age = Column(Integer)
    mark = Column(Float)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False
)
db = SessionLocal()

def get_db():
    db = SessionLocal()
    try: yield db
    finally : db.close()


def Useradd():
    newUser = tableModel(
        name = "Shivansh",
        age = 21,
        mark = 87.65
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    
def Userread():
    allUser = db.query(tableModel).all()
    print("Real All Data = ")
    print(allUser)

def Userupdate():
    user = db.query(tableModel).filter(
        tableModel.name == "Shivansh",
        tableModel.age == 21
    ).first()
    user.name = "Rahul"
    user.age = 25

    db.commit()
    db.refresh(user)

def Userdelete():
    user = db.query(tableModel).filter(
        tableModel.name == "Rahul",
        tableModel.age == 25
    ).first()
    db.delete(user)
    db.commit()





