from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from sqlalchemy import String , Column , Integer 
from fastapi import FastAPI , Depends


DATABASE_URL = "sqlite:///./check.db"
engine = create_engine(
DATABASE_URL,
connect_args={"check_same_thread":False}
)

Base = declarative_base()

class TableModel(Base):
    __tablename__ = "tata"

    id = Column(Integer , primary_key=True , index= True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

app = FastAPI()

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind=engine
)

def get_db():
    db = SessionLocal()

    try: yield db
    finally: db.close()

@app.get('/add')
def addUser(name :str , age:int , db : Session = Depends(get_db) ):
    newName = TableModel(
        name = name,
        age = age
    )
    

@app.get("/home")
def home():
    return{
        'message':'Hello Welcome Shivansh Kushwah'
    }
