from fastapi import APIRouter, HTTPException
from password_validator import PasswordValidator
from model.user_model import user
from confiq.confiq import operation
from serializaion.serialized import convert_user 

user_route = APIRouter()
schema = PasswordValidator()

@user_route.post("/user/signup")
def sign_up(user: user):
    try:
        user_dict = user.dict()
        user.id = len(user_dict) + 1
        if (user_dict["name"]== ""):
           raise HTTPException(status_code=404, detail = "user not found")
        elif (user_dict["email"]== ""):
            raise HTTPException(status_code=404, detail = "user not found")
        elif (user_dict["password"]== ""):
            raise HTTPException(status_code=404, detail = "user not found")
        result = operation.insert_one(user_dict)
        userResult = operation.find_one({"_id": result.inserted_id})
        return convert_user(userResult)
    except HTTPException as e:
        print(e)
    raise HTTPException(status_code=500, detail = {"message": "server not found"})
    
  
        




