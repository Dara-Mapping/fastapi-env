from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return{'data': {'name': 'Jonh Doe'}}

@app.get("/about")
def about():
    return {'data': {'about page'}}