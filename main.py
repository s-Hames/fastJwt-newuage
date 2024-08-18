# from fastapi import FastAPI
import uvicorn

if __name__ == "__main__":
    # uvicorn.run("app.api:app")
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)

# app = FastAPI()


# @app.get('/')
# def hello_world():
#     return "Hello,World"


# if __name__ == '__main__':
#     uvicorn.run(app)