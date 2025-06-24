from fastapi import FastAPI
from app.models.post_model import Base
from app.core.db import engine
import app.models.users_model
from app.routes import post_routes


app = FastAPI()

app.include_router(post_routes.router)


Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}