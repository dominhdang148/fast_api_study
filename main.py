from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def base_get_route():
    return {"message": "Hello from the GET route"}


@app.post('/')
async def post():
    return {"message": "Hello from the POST route"}


@app.put('/')
async def put():
    return {"message": "Hello from the PUT route"}


@app.delete('/')
async def delete():
    return {"message": "Hello from the DELETE route"}
