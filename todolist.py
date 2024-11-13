from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(docs_url='/tasks')
class TodoModel(BaseModel):
    id:int
    task:str
    description:str
    completed:bool
todos=[]
@app.get('/')
async def home():
    return ['welcome']
@app.post('/todos/')
async def post_todos(task:TodoModel):
    todos.append(task)
    return {"successfullly added":task.task}

@app.get('/get_tasks/')
async def get_all_todos():
    return todos

@app.get('/get_task/{id}')
async def get_task(id:int):
    for tasks in todos:
        if tasks.id==id:
            return tasks
    return {"error":"task is not found"}

@app.delete('/delete/{id}')
async def delete_task(id:int):
    for ind,tasks in enumerate(todos):
        if tasks.id==id:
            new=tasks
            todos.pop(ind)
            return {"successfully deleted":new}
    return {"error":"task is not found"}

@app.put("/todos/{id}")
def update_task(id: int, todo: TodoModel):
    for ind,tasks in enumerate(todos):
        if tasks.id==id:
            todos[ind]=todo
            return {"successfully deleted":todo}
    return {"error": "Task not found"}

