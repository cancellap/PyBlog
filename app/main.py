from fastapi import FastAPI
from app.models.post_model import Base
from app.core.db import engine
import app.models.users_model
from app.routes import login_routes, post_routes, user_routes


app = FastAPI()

app.include_router(post_routes.router, prefix="/posts", tags=["posts"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(login_routes.router, prefix="/auth", tags=["auth"])

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}