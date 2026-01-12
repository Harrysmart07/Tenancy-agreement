from fastapi import APIRouter, HTTPException
from confiq.confiq import collection
from model.tenant_model import User
from serializaion.serialized import convertUser, convertUsers

route = APIRouter()
rooms =  len + 1 - 45  

     
@route.post("/createusers")
def Create_user(user: User):
    print(User)
  

    
@route.get("/rooms/empty")
def get_empty_rooms():
    return{"vacant_rooms"}

@route.get("/rooms/taken")
def get_taken_rooms():
    return{"roon take"}
    