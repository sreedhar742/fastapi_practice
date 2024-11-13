from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def read_root():
    return {"name":"sreedhar"}

# @app.get('/items/{item_id}')
# def read_input(item_id:int):
#     return {'item_id':item_id}

# @app.get('/users/me') 
# def printnames():
#     return {"name":"sreedhar"}

# @app.get('/users/{name}')
# def returnnames(name):
#     return {'name':name}

# from enum import Enum
# class ModelName(str,Enum):
#     alexnet="alexnet",
#     resnet='resnet',
#     lenet='lenet'
# newapp=FastAPI()
# @newapp.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

from enum import Enum
class Model(str,Enum):
    firstname="chetan"
    lastname="jetty"
    fathername="nettappa"
    mothername="bhagyamma"
    
    
@app.get('/models/{model_name}')
def Modelnames(model_name:Model):
    if model_name==Model.firstname:
        return {"modelname":model_name,"details":"spring boot developer"}
    if model_name.value=="jetty":
        return {"modelname":model_name,"details":"django developer"}
    return {"father_name":Model.fathername,"mothername":Model.mothername}
        
        
        
student={
    1:{
        'firstname':"sreedhar",
        'lastname':"pedda pullannagar",
        'mothername':'bhagyamma',
        'fathername':'nettappa',
    }
}
# in fastapis path must be starts with /

@app.get('/get/{student_id}')
def students(student_id:int):
    return student[student_id]

@app.get('/items/{item_id}')
async def itemss(item_id):
    return {"items":item_id}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get('/fake_db/')
async def read_items(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]


