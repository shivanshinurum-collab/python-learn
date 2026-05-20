from pydantic import BaseModel
from fastapi import FastAPI
import sqlite3

db = sqlite3.connect("store.db",check_same_thread=False)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
name  TEXT,
count  INTEGER
)
""")

app = FastAPI()

@app.get("/showAll")
def showAll():
    cursor.execute("SELECT * FROM items")
    return{
        'data' : cursor.fetchall()
    }


class itemModel(BaseModel):
    name : str
    count : int


@app.post("/addItem")
def addItem(item : itemModel):
    cursor.execute("INSERT INTO items (name , count) VALUES (? , ?)",(item.name , item.count))
    db.commit()
    return{
        'message' : 'Successfully inserted Item',
        'status' : True
    }

@app.get("/findItem")
def singleItem(name : str):
    cursor.execute("SELECT * FROM items WHERE name == ?",(name,))
    return{
        "data" : cursor.fetchall()
    }

@app.delete("/deleteItem")
def deleteItem(name : str):
    cursor.execute("DELETE FROM items WHERE name == ?",(name,))
    db.commit()
    return{
        'message':'Successfully Deleted Item',
        'status':True
    }    


@app.put("/updateItem")
def updateItem(item : itemModel):
    cursor.execute("UPDATE items SET count = ? WHERE name = ?",(item.count , item.name))
    db.commit()
    return{
        'message' : "Successfully Update item Count",
        'status' : True
    }    