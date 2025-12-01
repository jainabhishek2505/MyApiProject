from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Temporary database
users_db = {}

# User model
class User(BaseModel):
    email: str
    password: str
    name: str = None


# ---------------------------
# SIGNUP API (Register User)
# ---------------------------
@app.post("/signup")
def signup(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Save user
    users_db[user.email] = {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    return {"message": "Signup successful!", "user": users_db[user.email]}


# ---------------------------
# LOGIN API
# ---------------------------
@app.post("/login")
def login(user: User):
    if user.email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    if users_db[user.email]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Wrong password")

    return {"message": "Login successful!", "user": users_db[user.email]}
