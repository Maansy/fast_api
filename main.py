from fastapi import FastAPI

app = FastAPI()

@app.get("/",description='First app', tags=["root"])
async def root():
    return {"message":"Hello world"}

@app.post("/", tags=["root"])
async def post():
    return {"message":"Hello from post"}

@app.put("/", tags=["root"])
async def put():
    return {"message":"Hello from put"}

@app.get("/hello/{name}", description='Hello to the user', tags=["hello"])
async def hello_name(name):
    return {"message":f"Hello {name}"}