from fastapi import FastAPI

app = FastAPI()

@app.get("/posts")
def list_posts():
    return [{"id": 1, "title": "Hello World"}]
