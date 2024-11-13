from fastapi import APIRouter, FastAPI

app = FastAPI(debug=True)
router1 = APIRouter()
router2=APIRouter()

@router1.get("/users-profiles/", tags=["user-profiles"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router1.get("/user_names1/",tags=["user_names"])
async def read_user_names():
    return [{"name1":"Sreedhar","name2":"Chetan","name3":"Sunil"}]

@router2.get('/books',tags=["user_books"])
async def read_inputs():
    return [{"bookaname":"meinkhempf","author":"adolf hitler"}]
@router2.get("/user_names2/",tags=["user_names from router 2"])
async def read_user_names():
    return [{"name1":"Sreedhar","name2":"Chetan","name3":"Sunil"}]

app.include_router(router1)

app.include_router(router2)
