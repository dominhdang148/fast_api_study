from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def base_get_route():
    return {"message": "Hello World"}


@app.post('/')
async def post():
    return {"message": "Hello from the POST route"}


@app.put('/')
async def put():
    return {"message": "Hello from the PUT route"}
