from models import Todo
import motor.motor_asyncio
client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database=client.TodoList
collection=database.todo


async def find_one_todo(title):
    document=await collection.find_one({"title":title})
    return document

async def find_all_todo(): 
    todos=[]
    cursor=collection.find({})
    async for doc in cursor:
        todos.append(Todo(**doc))
    return todos

async def create_todo(todo):
    document=todo
    result=await collection.insert_one(document)
    return document

async def update_todo(tit,desc):
    await collection.update_one({'title':tit},{'$set':{'description':desc}})
    document=await collection.find_one({'title':tit})
    return document


async def remove_todo(title):
    await collection.delete_one({'title':title})
    return True