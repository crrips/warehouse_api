from fastapi import FastAPI
from models.base import Base
import uvicorn
from endpoints import get_router
from db import engine


app = FastAPI()
app.include_router(get_router())
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    