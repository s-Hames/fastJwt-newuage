# from fastapi import FastAPI
import uvicorn

if __name__ == "__main__":
    # uvicorn.run("app.api:app")
    uvicorn.run("app.api:app")

# app = FastAPI()


# @app.get('/')
# def hello_world():
#     return "Hello,World"


# if __name__ == '__main__':
#     uvicorn.run(app)