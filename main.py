# from fastapi import FastAPI
import uvicorn
from app import api

if __name__ == "__main__":
    uvicorn.run(api.app)

# app = FastAPI()


# @app.get('/')
# def hello_world():
#     return "Hello,World"


# if __name__ == '__main__':
#     uvicorn.run(app)