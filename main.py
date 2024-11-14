from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import find_one_todo, find_all_todo, create_todo, update_todo, remove_todo
import motor.motor_asyncio

app = FastAPI()


origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.TodoList
collection = database.Todo

@app.on_event("startup")
async def startup_db_client():
    try:
      
        await client.admin.command("ping")
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print("Failed to connect to MongoDB:", e)


from models import Todo

# Define endpoints
@app.get('/')
async def read_roots():
    return {"ping": "pong"}

@app.get('/api/todo')
async def get_todo():
    response = await find_all_todo()
    return response

@app.get('/api/todo/{title}', response_model=Todo)
async def get_one_todo(title: str):
    response = await find_one_todo(title)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"Todo not found: {title}")

@app.post('/api/todo', response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@app.put('/api/todo/{title}', response_model=Todo)
async def put_todo(title: str, description: str):
    response = await update_todo(title, description)
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")

@app.delete('/api/todo/{title}')
async def del_todo(title: str):
    response = await remove_todo(title)
    if response:
        return {"message": "Successfully deleted"}
    raise HTTPException(status_code=400, detail="Something went wrong")
