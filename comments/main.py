from fastapi import FastAPI

app = FastAPI()

@app.get("/comments/{post_id}")
def list_comments(post_id: int):
    return [{"post_id": post_id, "comment": "Nice post!"}]
