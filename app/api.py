

from fastapi import Depends, FastAPI, Body
import uvicorn

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
from app.model import UserSchema, UserLoginSchema
    
app = FastAPI()
if __name__ == "__main__":
    uvicorn.run(app)
users = []


@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to your blog!"}

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return sign_jwt(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }

@app.get('/test',dependencies=[Depends(JWTBearer())])
def testJWT() :
    return {
        "message" : "verified user hai bhai sending data"
    }
